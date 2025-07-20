#!/usr/bin/env python3
"""
InfoBlox Network Updater - Applies changes from analysis

This script takes the analysis results and applies the necessary changes:
1. Creates network containers and networks in hierarchical order
2. Updates extended attributes (tags)
3. Handles conflicts safely
4. Provides detailed logging and rollback capability

Author: AWS-InfoBlox Integration Team
Date: January 2025
"""

import json
import logging
import sys
import os
import ipaddress
from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
import requests
import urllib3
from dotenv import load_dotenv
import argparse
import csv
import time

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('infoblox_network_updater.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NetworkUpdater:
    """Handles network creation and updates in InfoBlox"""
    
    def __init__(self, ib_client, network_view: str, dry_run: bool = False):
        self.ib_client = ib_client
        self.network_view = network_view
        self.dry_run = dry_run
        self.created_objects = []  # Track for potential rollback
        self.update_log = []
        self.error_log = []
        
    def apply_updates(self, analysis_results: Dict) -> Dict:
        """Apply all updates from analysis results"""
        summary = {
            'containers_created': 0,
            'networks_created': 0,
            'tags_updated': 0,
            'errors': 0,
            'start_time': datetime.now(),
            'end_time': None
        }
        
        try:
            # Phase 1: Create containers first (hierarchical order)
            logger.info("Phase 1: Creating network containers...")
            self._create_containers(analysis_results, summary)
            
            # Phase 2: Create regular networks
            logger.info("Phase 2: Creating networks...")
            self._create_networks(analysis_results, summary)
            
            # Phase 3: Update tags/extended attributes
            logger.info("Phase 3: Updating extended attributes...")
            self._update_tags(analysis_results, summary)
            
        except Exception as e:
            logger.error(f"Critical error during updates: {e}")
            if not self.dry_run:
                self._rollback()
            raise
        finally:
            summary['end_time'] = datetime.now()
            self._generate_update_report(summary)
        
        return summary
    
    def _create_containers(self, analysis_results: Dict, summary: Dict):
        """Create network containers in proper order"""
        containers = [n for n in analysis_results['proposed_networks'] if n['type'] == 'CONTAINER']
        
        # Sort by prefix length (larger networks first)
        containers.sort(key=lambda x: int(x['cidr'].split('/')[1]))
        
        for container in containers:
            try:
                if self._create_network_container(container):
                    summary['containers_created'] += 1
                    self.update_log.append({
                        'action': 'CREATE_CONTAINER',
                        'network': container['cidr'],
                        'status': 'SUCCESS',
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    summary['errors'] += 1
            except Exception as e:
                logger.error(f"Error creating container {container['cidr']}: {e}")
                summary['errors'] += 1
                self.error_log.append({
                    'action': 'CREATE_CONTAINER',
                    'network': container['cidr'],
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
    
    def _create_networks(self, analysis_results: Dict, summary: Dict):
        """Create regular networks"""
        networks = [n for n in analysis_results['proposed_networks'] if n['type'] == 'NETWORK']
        
        # Sort by prefix length (smaller networks last)
        networks.sort(key=lambda x: int(x['cidr'].split('/')[1]))
        
        for network in networks:
            try:
                if self._create_network(network):
                    summary['networks_created'] += 1
                    self.update_log.append({
                        'action': 'CREATE_NETWORK',
                        'network': network['cidr'],
                        'status': 'SUCCESS',
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    summary['errors'] += 1
            except Exception as e:
                logger.error(f"Error creating network {network['cidr']}: {e}")
                summary['errors'] += 1
                self.error_log.append({
                    'action': 'CREATE_NETWORK',
                    'network': network['cidr'],
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
    
    def _update_tags(self, analysis_results: Dict, summary: Dict):
        """Update extended attributes for existing networks"""
        for discrepancy in analysis_results['tag_discrepancies']:
            try:
                if self._update_network_tags(discrepancy):
                    summary['tags_updated'] += 1
                    self.update_log.append({
                        'action': 'UPDATE_TAGS',
                        'network': discrepancy['network'],
                        'status': 'SUCCESS',
                        'timestamp': datetime.now().isoformat()
                    })
                else:
                    summary['errors'] += 1
            except Exception as e:
                logger.error(f"Error updating tags for {discrepancy['network']}: {e}")
                summary['errors'] += 1
                self.error_log.append({
                    'action': 'UPDATE_TAGS',
                    'network': discrepancy['network'],
                    'error': str(e),
                    'timestamp': datetime.now().isoformat()
                })
    
    def _create_network_container(self, container: Dict) -> bool:
        """Create a network container in InfoBlox"""
        if self.dry_run:
            logger.info(f"[DRY RUN] Would create container: {container['cidr']}")
            return True
        
        data = {
            'network': container['cidr'],
            'network_view': self.network_view,
            'comment': f"Created from AWS export - {datetime.now().strftime('%Y-%m-%d')}"
        }
        
        # Add extended attributes
        if container.get('tags'):
            data['extattrs'] = self._format_extended_attributes(container['tags'])
        
        try:
            response = self.ib_client.session.post(
                f"{self.ib_client.base_url}/networkcontainer",
                json=data
            )
            
            if response.status_code == 201:
                self.created_objects.append({
                    'ref': response.json(),
                    'type': 'networkcontainer'
                })
                logger.info(f"✅ Created container: {container['cidr']}")
                return True
            else:
                logger.error(f"Failed to create container {container['cidr']}: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Exception creating container: {e}")
            raise
    
    def _create_network(self, network: Dict) -> bool:
        """Create a network in InfoBlox"""
        if self.dry_run:
            logger.info(f"[DRY RUN] Would create network: {network['cidr']}")
            return True
        
        data = {
            'network': network['cidr'],
            'network_view': self.network_view,
            'comment': f"Created from AWS export - {datetime.now().strftime('%Y-%m-%d')}"
        }
        
        # Add extended attributes
        if network.get('tags'):
            data['extattrs'] = self._format_extended_attributes(network['tags'])
        
        try:
            response = self.ib_client.session.post(
                f"{self.ib_client.base_url}/network",
                json=data
            )
            
            if response.status_code == 201:
                self.created_objects.append({
                    'ref': response.json(),
                    'type': 'network'
                })
                logger.info(f"✅ Created network: {network['cidr']}")
                return True
            else:
                logger.error(f"Failed to create network {network['cidr']}: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Exception creating network: {e}")
            raise
    
    def _update_network_tags(self, discrepancy: Dict) -> bool:
        """Update extended attributes for an existing network"""
        if self.dry_run:
            logger.info(f"[DRY RUN] Would update tags for: {discrepancy['network']}")
            return True
        
        try:
            # First, find the network
            response = self.ib_client.session.get(
                f"{self.ib_client.base_url}/network",
                params={
                    'network': discrepancy['network'],
                    'network_view': self.network_view,
                    '_return_fields': '_ref,extattrs'
                }
            )
            
            if response.status_code == 200 and response.json():
                network = response.json()[0]
                network_ref = network['_ref']
                current_eas = network.get('extattrs', {})
                
                # Merge tags
                updated_eas = current_eas.copy()
                
                # Add missing tags
                for key, value in discrepancy['missing_tags'].items():
                    updated_eas[key] = {'value': value}
                
                # Update changed tags
                for key, changes in discrepancy['updated_tags'].items():
                    updated_eas[key] = {'value': changes['new_value']}
                
                # Update the network
                update_response = self.ib_client.session.put(
                    f"{self.ib_client.base_url}/{network_ref}",
                    json={'extattrs': updated_eas}
                )
                
                if update_response.status_code == 200:
                    logger.info(f"✅ Updated tags for: {discrepancy['network']}")
                    return True
                else:
                    logger.error(f"Failed to update tags: {update_response.text}")
                    return False
            else:
                logger.error(f"Network not found: {discrepancy['network']}")
                return False
                
        except Exception as e:
            logger.error(f"Exception updating tags: {e}")
            raise
    
    def _format_extended_attributes(self, tags: Dict) -> Dict:
        """Format tags for InfoBlox extended attributes"""
        eas = {}
        for key, value in tags.items():
            eas[key] = {'value': str(value)}
        return eas
    
    def _rollback(self):
        """Rollback created objects in case of error"""
        logger.warning("Initiating rollback of created objects...")
        
        # Reverse order - delete in opposite order of creation
        for obj in reversed(self.created_objects):
            try:
                response = self.ib_client.session.delete(
                    f"{self.ib_client.base_url}/{obj['ref']}"
                )
                if response.status_code == 200:
                    logger.info(f"Rolled back: {obj['ref']}")
                else:
                    logger.error(f"Failed to rollback: {obj['ref']}")
            except Exception as e:
                logger.error(f"Error during rollback: {e}")
    
    def _generate_update_report(self, summary: Dict):
        """Generate detailed update report"""
        report_dir = f"reports/updates_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(report_dir, exist_ok=True)
        
        # Write summary
        summary_file = os.path.join(report_dir, 'update_summary.txt')
        with open(summary_file, 'w') as f:
            f.write("InfoBlox Network Update Summary\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Start Time: {summary['start_time']}\n")
            f.write(f"End Time: {summary['end_time']}\n")
            f.write(f"Duration: {summary['end_time'] - summary['start_time']}\n\n")
            f.write(f"Containers Created: {summary['containers_created']}\n")
            f.write(f"Networks Created: {summary['networks_created']}\n")
            f.write(f"Tags Updated: {summary['tags_updated']}\n")
            f.write(f"Errors: {summary['errors']}\n")
        
        # Write detailed logs
        if self.update_log:
            update_file = os.path.join(report_dir, 'successful_updates.csv')
            with open(update_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['timestamp', 'action', 'network', 'status'])
                writer.writeheader()
                writer.writerows(self.update_log)
        
        if self.error_log:
            error_file = os.path.join(report_dir, 'failed_updates.csv')
            with open(error_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['timestamp', 'action', 'network', 'error'])
                writer.writeheader()
                writer.writerows(self.error_log)
        
        logger.info(f"Update report generated: {report_dir}")


class InfoBloxClient:
    """InfoBlox API Client"""
    
    def __init__(self, grid_master: str, username: str, password: str):
        self.grid_master = grid_master
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.verify = False
        self.base_url = f"https://{grid_master}/wapi/v2.13.1"
        
        # Test connection
        self._test_connection()
    
    def _test_connection(self):
        """Test connection to InfoBlox"""
        try:
            response = self.session.get(f"{self.base_url}/grid")
            response.raise_for_status()
            logger.info("✅ Successfully connected to InfoBlox")
        except Exception as e:
            logger.error(f"Failed to connect to InfoBlox: {e}")
            raise


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Apply network updates from analysis results'
    )
    parser.add_argument(
        'analysis_file',
        help='Path to analysis results JSON file'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Simulate changes without applying them'
    )
    parser.add_argument(
        '--network-view',
        help='Override network view from analysis',
        default=None
    )
    parser.add_argument(
        '--skip-containers',
        action='store_true',
        help='Skip container creation'
    )
    parser.add_argument(
        '--skip-networks',
        action='store_true',
        help='Skip network creation'
    )
    parser.add_argument(
        '--skip-tags',
        action='store_true',
        help='Skip tag updates'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        default=50,
        help='Number of operations per batch (default: 50)'
    )
    return parser.parse_args()


def load_analysis_results(file_path: str) -> Dict:
    """Load analysis results from JSON file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading analysis results: {e}")
        raise


def main():
    """Main execution function"""
    load_dotenv('config.env')
    args = parse_arguments()
    
    # Get configuration
    grid_master = os.getenv('GRID_MASTER', 'infoblox.example.com')
    username = os.getenv('INFOBLOX_USERNAME') or input("InfoBlox username: ")
    import getpass
    password = os.getenv('INFOBLOX_PASSWORD') or getpass.getpass("InfoBlox password: ")
    
    try:
        # Load analysis results
        logger.info(f"Loading analysis results from {args.analysis_file}")
        analysis_results = load_analysis_results(args.analysis_file)
        
        # Override network view if specified
        network_view = args.network_view or analysis_results.get('network_view', 'default')
        
        # Filter operations based on command line options
        if args.skip_containers:
            analysis_results['proposed_networks'] = [
                n for n in analysis_results['proposed_networks'] 
                if n['type'] != 'CONTAINER'
            ]
        
        if args.skip_networks:
            analysis_results['proposed_networks'] = [
                n for n in analysis_results['proposed_networks'] 
                if n['type'] != 'NETWORK'
            ]
        
        if args.skip_tags:
            analysis_results['tag_discrepancies'] = []
        
        # Initialize InfoBlox client
        ib_client = InfoBloxClient(grid_master, username, password)
        
        # Initialize updater
        updater = NetworkUpdater(ib_client, network_view, dry_run=args.dry_run)
        
        # Show summary of planned changes
        print(f"\n📋 Planned Changes Summary:")
        print(f"   - Containers to create: {len([n for n in analysis_results['proposed_networks'] if n['type'] == 'CONTAINER'])}")
        print(f"   - Networks to create: {len([n for n in analysis_results['proposed_networks'] if n['type'] == 'NETWORK'])}")
        print(f"   - Tags to update: {len(analysis_results['tag_discrepancies'])}")
        
        if args.dry_run:
            print("\n🔍 DRY RUN MODE - No changes will be made")
        else:
            response = input("\n⚠️  Proceed with updates? (yes/no): ")
            if response.lower() != 'yes':
                print("Update cancelled.")
                return 0
        
        # Apply updates
        summary = updater.apply_updates(analysis_results)
        
        # Print summary
        print(f"\n✅ Update Complete!")
        print(f"   - Containers created: {summary['containers_created']}")
        print(f"   - Networks created: {summary['networks_created']}")
        print(f"   - Tags updated: {summary['tags_updated']}")
        print(f"   - Errors: {summary['errors']}")
        print(f"   - Duration: {summary['end_time'] - summary['start_time']}")
        
        if summary['errors'] > 0:
            print("\n⚠️  Some operations failed. Check the error log for details.")
            return 1
        
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())