#!/usr/bin/env python3
"""
InfoBlox vs AWS Network Comprehensive Analyzer

This tool performs comprehensive analysis between AWS export data and existing InfoBlox networks:
1. Identifies networks in InfoBlox but not in AWS export (no deletes)
2. Detects conflicts between subnets
3. Creates hierarchical network containers (/16 -> /24 -> /27)
4. Preserves and compares all tags
5. Generates web reports with downloadable CSV lists

Author: AWS-InfoBlox Integration Team
Date: January 2025
"""

import pandas as pd
import requests
import json
import urllib3
import logging
import ipaddress
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Set, Any
import argparse
import os
from dotenv import load_dotenv
import getpass
import sys
from collections import defaultdict
import csv
from jinja2 import Template

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('infoblox_aws_analyzer.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class NetworkAnalyzer:
    """Comprehensive network analysis between AWS and InfoBlox"""
    
    def __init__(self, ib_client, network_view: str):
        self.ib_client = ib_client
        self.network_view = network_view
        self.analysis_results = {
            'orphaned_networks': [],      # Networks in InfoBlox but not in AWS
            'conflicts': [],              # Conflicting subnets
            'hierarchy': {},              # Network hierarchy mapping
            'tag_discrepancies': [],      # Tag differences
            'proposed_containers': [],    # Networks that should be containers
            'proposed_networks': [],      # Networks to be created
            'timestamp': datetime.now().strftime('%Y%m%d_%H%M%S')
        }
    
    def analyze_networks(self, aws_networks: List[Dict], infoblox_networks: List[Dict]) -> Dict:
        """Perform comprehensive network analysis"""
        logger.info("Starting comprehensive network analysis...")
        
        # Step 1: Find orphaned networks (in InfoBlox but not in AWS)
        self._find_orphaned_networks(aws_networks, infoblox_networks)
        
        # Step 2: Analyze network hierarchy and detect conflicts
        self._analyze_hierarchy_and_conflicts(aws_networks, infoblox_networks)
        
        # Step 3: Compare tags/extended attributes
        self._compare_tags(aws_networks, infoblox_networks)
        
        # Step 4: Generate proposed actions
        self._generate_proposed_actions(aws_networks, infoblox_networks)
        
        return self.analysis_results
    
    def _find_orphaned_networks(self, aws_networks: List[Dict], infoblox_networks: List[Dict]):
        """Find AWS-sourced networks in InfoBlox that are not in current AWS export"""
        aws_cidrs = {net['cidr'] for net in aws_networks}
        
        for ib_net in infoblox_networks:
            # Only consider networks that are marked as AWS-sourced
            eas = ib_net.get('extattrs', {})
            source = eas.get('Source', {}).get('value', '').upper()
            cloud_provider = eas.get('Cloud_Provider', {}).get('value', '').upper()
            
            # Check if this is an AWS network (by EA tags or comments)
            is_aws_network = (
                source == 'AWS' or 
                cloud_provider == 'AWS' or
                'AWS' in ib_net.get('comment', '').upper()
            )
            
            # Only flag AWS networks that aren't in the current export
            if is_aws_network and ib_net['network'] not in aws_cidrs:
                self.analysis_results['orphaned_networks'].append({
                    'network': ib_net['network'],
                    'type': ib_net.get('_type', 'network'),
                    'extended_attributes': ib_net.get('extattrs', {}),
                    'comment': ib_net.get('comment', ''),
                    'source': source or cloud_provider or 'AWS (inferred)',
                    'action': 'REVIEW_FOR_DELETION'
                })
        
        logger.info(f"Found {len(self.analysis_results['orphaned_networks'])} orphaned AWS networks")
    
    def _analyze_hierarchy_and_conflicts(self, aws_networks: List[Dict], infoblox_networks: List[Dict]):
        """Analyze network hierarchy and detect conflicts"""
        # Create network objects for comparison
        aws_net_objects = []
        for net in aws_networks:
            try:
                aws_net_objects.append({
                    'network': ipaddress.ip_network(net['cidr'], strict=False),
                    'cidr': net['cidr'],
                    'data': net
                })
            except ValueError:
                logger.error(f"Invalid CIDR: {net['cidr']}")
        
        # Sort by prefix length (larger networks first)
        aws_net_objects.sort(key=lambda x: x['network'].prefixlen)
        
        # Build hierarchy and detect conflicts
        hierarchy = defaultdict(list)
        conflicts = []
        
        for i, net1 in enumerate(aws_net_objects):
            for j, net2 in enumerate(aws_net_objects[i+1:], i+1):
                if net1['network'].supernet_of(net2['network']):
                    # net1 contains net2 - this is hierarchical
                    hierarchy[net1['cidr']].append(net2['cidr'])
                elif net1['network'].overlaps(net2['network']) and not net2['network'].supernet_of(net1['network']):
                    # Partial overlap - this is a conflict
                    conflicts.append({
                        'network1': net1['cidr'],
                        'network2': net2['cidr'],
                        'type': 'PARTIAL_OVERLAP',
                        'severity': 'HIGH'
                    })
        
        # Check for conflicts with ALL existing InfoBlox networks (regardless of source)
        for aws_net in aws_net_objects:
            contained_networks = []
            
            for ib_net in infoblox_networks:
                try:
                    ib_network = ipaddress.ip_network(ib_net['network'], strict=False)
                    if aws_net['network'].overlaps(ib_network):
                        # Get source information
                        eas = ib_net.get('extattrs', {})
                        ib_source = (eas.get('Source', {}).get('value') or 
                                   eas.get('Cloud_Provider', {}).get('value') or 
                                   'Unknown')
                        
                        # Determine conflict type
                        if aws_net['network'] == ib_network:
                            # Exact match - check if it's AWS sourced
                            if ib_source.upper() != 'AWS':
                                conflicts.append({
                                    'network1': aws_net['cidr'],
                                    'network2': ib_net['network'],
                                    'type': 'EXACT_MATCH_DIFFERENT_SOURCE',
                                    'severity': 'CRITICAL',
                                    'existing_source': ib_source,
                                    'existing_network': True
                                })
                        elif aws_net['network'].supernet_of(ib_network):
                            # AWS network contains existing network
                            contained_networks.append({
                                'network': ib_net['network'],
                                'source': ib_source,
                                'type': ib_net.get('_type', 'network')
                            })
                        elif ib_network.supernet_of(aws_net['network']):
                            # Existing network contains AWS network
                            if ib_net.get('_type') == 'network':
                                # Regular network acting as container - conflict
                                conflicts.append({
                                    'network1': aws_net['cidr'],
                                    'network2': ib_net['network'],
                                    'type': 'CONTAINED_BY_NON_CONTAINER',
                                    'severity': 'HIGH',
                                    'existing_source': ib_source,
                                    'existing_network': True
                                })
                        else:
                            # Partial overlap conflict
                            conflicts.append({
                                'network1': aws_net['cidr'],
                                'network2': ib_net['network'],
                                'type': 'PARTIAL_OVERLAP',
                                'severity': 'CRITICAL',
                                'existing_source': ib_source,
                                'existing_network': True
                            })
                except ValueError:
                    logger.error(f"Invalid network in InfoBlox: {ib_net.get('network')}")
            
            # If AWS network contains other networks, it should be a container
            if contained_networks:
                self.analysis_results['proposed_containers'].append({
                    'cidr': aws_net['cidr'],
                    'reason': f"Contains {len(contained_networks)} existing network(s)",
                    'contained_networks': contained_networks
                })
        
        self.analysis_results['hierarchy'] = dict(hierarchy)
        self.analysis_results['conflicts'] = conflicts
        logger.info(f"Found {len(conflicts)} conflicts and built hierarchy with {len(hierarchy)} containers")
    
    def _compare_tags(self, aws_networks: List[Dict], infoblox_networks: List[Dict]):
        """Compare tags between AWS and InfoBlox for AWS-sourced networks only"""
        # Create lookup map for InfoBlox networks
        ib_network_map = {net['network']: net for net in infoblox_networks}
        
        for aws_net in aws_networks:
            if aws_net['cidr'] in ib_network_map:
                ib_net = ib_network_map[aws_net['cidr']]
                ib_eas = ib_net.get('extattrs', {})
                
                # Check if this is an AWS-sourced network
                ib_source = (ib_eas.get('Source', {}).get('value', '').upper() or 
                           ib_eas.get('Cloud_Provider', {}).get('value', '').upper())
                
                # Only update tags for AWS-sourced networks
                if ib_source in ['AWS', '']:  # Empty source might be AWS
                    aws_tags = aws_net.get('tags', {})
                    
                    # Always ensure Source is set to AWS
                    if 'Source' not in ib_eas or ib_eas.get('Source', {}).get('value', '').upper() != 'AWS':
                        aws_tags['Source'] = 'AWS'
                    
                    # Find missing tags in InfoBlox
                    missing_tags = {}
                    updated_tags = {}
                    
                    for tag_key, tag_value in aws_tags.items():
                        if tag_key not in ib_eas:
                            missing_tags[tag_key] = tag_value
                        elif str(ib_eas[tag_key].get('value', '')) != str(tag_value):
                            updated_tags[tag_key] = {
                                'old_value': ib_eas[tag_key].get('value'),
                                'new_value': tag_value
                            }
                    
                    if missing_tags or updated_tags:
                        self.analysis_results['tag_discrepancies'].append({
                            'network': aws_net['cidr'],
                            'missing_tags': missing_tags,
                            'updated_tags': updated_tags,
                            'current_source': ib_source or 'Unknown',
                            'action': 'UPDATE_TAGS'
                        })
                else:
                    # Network exists but belongs to different source - this is a conflict
                    logger.warning(f"Network {aws_net['cidr']} exists but is sourced from {ib_source}")
        
        logger.info(f"Found {len(self.analysis_results['tag_discrepancies'])} AWS networks with tag discrepancies")
    
    def _generate_proposed_actions(self, aws_networks: List[Dict], infoblox_networks: List[Dict]):
        """Generate proposed actions for network creation/updates"""
        existing_cidrs = {net['network'] for net in infoblox_networks}
        
        # Determine which networks need to be created
        for aws_net in aws_networks:
            if aws_net['cidr'] not in existing_cidrs:
                # Check if this should be a container
                is_container = (aws_net['cidr'] in self.analysis_results['hierarchy'] or
                              any(pc['cidr'] == aws_net['cidr'] for pc in self.analysis_results['proposed_containers']))
                
                # Ensure Source tag is set
                tags = aws_net.get('tags', {}).copy()
                tags['Source'] = 'AWS'
                
                self.analysis_results['proposed_networks'].append({
                    'cidr': aws_net['cidr'],
                    'type': 'CONTAINER' if is_container else 'NETWORK',
                    'tags': tags,
                    'priority': int(aws_net['cidr'].split('/')[1])  # Lower prefix = higher priority
                })
        
        # Sort by priority (containers first, then by prefix length)
        self.analysis_results['proposed_networks'].sort(
            key=lambda x: (0 if x['type'] == 'CONTAINER' else 1, x['priority'])
        )
        
        logger.info(f"Proposed {len(self.analysis_results['proposed_networks'])} new networks/containers")


class ReportGenerator:
    """Generate HTML reports with downloadable CSV files"""
    
    def __init__(self, analysis_results: Dict):
        self.results = analysis_results
        self.report_dir = f"reports/analysis_{analysis_results['timestamp']}"
        os.makedirs(self.report_dir, exist_ok=True)
    
    def generate_full_report(self) -> str:
        """Generate comprehensive HTML report"""
        # Generate CSV files
        csv_files = self._generate_csv_files()
        
        # Generate HTML report
        html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>InfoBlox vs AWS Network Analysis Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; }
        h2 { color: #666; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .summary { background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; }
        .critical { color: #d32f2f; font-weight: bold; }
        .warning { color: #f57c00; font-weight: bold; }
        .info { color: #1976d2; }
        table { border-collapse: collapse; width: 100%; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .download-btn { 
            background: #4CAF50; 
            color: white; 
            padding: 10px 20px; 
            text-decoration: none; 
            border-radius: 5px; 
            display: inline-block;
            margin: 5px;
        }
        .download-btn:hover { background: #45a049; }
        .action-required { background: #fff3cd; padding: 10px; border-left: 5px solid #f57c00; }
    </style>
</head>
<body>
    <h1>InfoBlox vs AWS Network Analysis Report</h1>
    <p>Generated: {{ timestamp }}</p>
    
    <div class="summary">
        <h2>Executive Summary</h2>
        <ul>
            <li>Orphaned AWS Networks (AWS-sourced in InfoBlox but not in current export): <span class="warning">{{ orphaned_count }}</span></li>
            <li>Network Conflicts: <span class="critical">{{ conflict_count }}</span></li>
            <li>Tag Discrepancies: <span class="info">{{ tag_discrepancy_count }}</span></li>
            <li>Proposed New Containers: {{ container_count }}</li>
            <li>Proposed New Networks: {{ network_count }}</li>
        </ul>
    </div>
    
    <div class="action-required">
        <h3>Actions Required:</h3>
        <ol>
            <li><strong>Review Orphaned Networks:</strong> Networks that exist in InfoBlox but not in AWS export need manual review for potential deletion.</li>
            <li><strong>Resolve Conflicts:</strong> Critical conflicts must be resolved before proceeding with network creation.</li>
            <li><strong>Update Tags:</strong> Extended attributes need to be updated to match AWS tags.</li>
            <li><strong>Create Networks:</strong> New networks and containers should be created in hierarchical order.</li>
        </ol>
    </div>
    
    <h2>Downloadable Reports</h2>
    <div>
        {% for file in csv_files %}
        <a href="{{ file.filename }}" class="download-btn" download>Download {{ file.name }}</a>
        {% endfor %}
    </div>
    
    <h2>Detailed Analysis</h2>
    
    <h3>1. Orphaned AWS Networks ({{ orphaned_count }} found)</h3>
    <p class="info">These are networks marked as AWS-sourced in InfoBlox but not present in the current AWS export.</p>
    {% if orphaned_networks %}
    <table>
        <tr>
            <th>Network</th>
            <th>Type</th>
            <th>Source</th>
            <th>Extended Attributes</th>
            <th>Action</th>
        </tr>
        {% for net in orphaned_networks[:10] %}
        <tr>
            <td>{{ net.network }}</td>
            <td>{{ net.type }}</td>
            <td>{{ net.source }}</td>
            <td>{{ net.extended_attributes }}</td>
            <td class="warning">{{ net.action }}</td>
        </tr>
        {% endfor %}
    </table>
    {% if orphaned_count > 10 %}
    <p><em>Showing first 10 of {{ orphaned_count }} orphaned AWS networks. Download full list for complete details.</em></p>
    {% endif %}
    {% else %}
    <p>No orphaned AWS networks found.</p>
    {% endif %}
    
    <h3>2. Network Conflicts ({{ conflict_count }} found)</h3>
    <p class="info">Conflicts with existing networks from any source (AWS, Azure, GCP, on-premises, etc.)</p>
    {% if conflicts %}
    <table>
        <tr>
            <th>AWS Network</th>
            <th>Existing Network</th>
            <th>Existing Source</th>
            <th>Conflict Type</th>
            <th>Severity</th>
        </tr>
        {% for conflict in conflicts[:10] %}
        <tr>
            <td>{{ conflict.network1 }}</td>
            <td>{{ conflict.network2 }}</td>
            <td>{{ conflict.existing_source if conflict.existing_source else 'Unknown' }}</td>
            <td>{{ conflict.type }}</td>
            <td class="{{ 'critical' if conflict.severity == 'CRITICAL' else 'warning' }}">
                {{ conflict.severity }}
            </td>
        </tr>
        {% endfor %}
    </table>
    {% if conflict_count > 10 %}
    <p><em>Showing first 10 of {{ conflict_count }} conflicts. Download full list for complete details.</em></p>
    {% endif %}
    {% else %}
    <p>No conflicts found.</p>
    {% endif %}
    
    <h3>3. Network Hierarchy</h3>
    {% if hierarchy %}
    <p>The following networks will be created as containers:</p>
    <ul>
        {% for container, children in hierarchy.items() %}
        <li><strong>{{ container }}</strong> (contains {{ children|length }} networks)</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No hierarchical relationships found.</p>
    {% endif %}
    
    <h3>4. Tag Discrepancies ({{ tag_discrepancy_count }} found)</h3>
    {% if tag_discrepancies %}
    <table>
        <tr>
            <th>Network</th>
            <th>Missing Tags</th>
            <th>Updated Tags</th>
            <th>Action</th>
        </tr>
        {% for disc in tag_discrepancies[:10] %}
        <tr>
            <td>{{ disc.network }}</td>
            <td>{{ disc.missing_tags }}</td>
            <td>{{ disc.updated_tags }}</td>
            <td class="info">{{ disc.action }}</td>
        </tr>
        {% endfor %}
    </table>
    {% if tag_discrepancy_count > 10 %}
    <p><em>Showing first 10 of {{ tag_discrepancy_count }} discrepancies. Download full list for complete details.</em></p>
    {% endif %}
    {% else %}
    <p>All tags are synchronized.</p>
    {% endif %}
    
    <h3>5. Proposed Network Creation Order</h3>
    {% if proposed_networks %}
    <table>
        <tr>
            <th>Priority</th>
            <th>Network</th>
            <th>Type</th>
            <th>Tags</th>
        </tr>
        {% for net in proposed_networks[:20] %}
        <tr>
            <td>{{ loop.index }}</td>
            <td>{{ net.cidr }}</td>
            <td>{{ net.type }}</td>
            <td>{{ net.tags }}</td>
        </tr>
        {% endfor %}
    </table>
    {% if proposed_networks|length > 20 %}
    <p><em>Showing first 20 of {{ proposed_networks|length }} proposed networks. Download full list for complete details.</em></p>
    {% endif %}
    {% else %}
    <p>No new networks to create.</p>
    {% endif %}
    
</body>
</html>
        '''
        
        template = Template(html_template)
        html_content = template.render(
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            orphaned_count=len(self.results['orphaned_networks']),
            orphaned_networks=self.results['orphaned_networks'],
            conflict_count=len(self.results['conflicts']),
            conflicts=self.results['conflicts'],
            tag_discrepancy_count=len(self.results['tag_discrepancies']),
            tag_discrepancies=self.results['tag_discrepancies'],
            hierarchy=self.results['hierarchy'],
            container_count=len([n for n in self.results['proposed_networks'] if n['type'] == 'CONTAINER']),
            network_count=len([n for n in self.results['proposed_networks'] if n['type'] == 'NETWORK']),
            proposed_networks=self.results['proposed_networks'],
            csv_files=csv_files
        )
        
        # Save HTML report
        report_path = os.path.join(self.report_dir, 'analysis_report.html')
        with open(report_path, 'w') as f:
            f.write(html_content)
        
        logger.info(f"Report generated: {report_path}")
        return report_path
    
    def _generate_csv_files(self) -> List[Dict]:
        """Generate CSV files for each analysis category"""
        csv_files = []
        
        # 1. Orphaned Networks CSV
        if self.results['orphaned_networks']:
            filename = 'orphaned_aws_networks.csv'
            filepath = os.path.join(self.report_dir, filename)
            with open(filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['network', 'type', 'source', 'extended_attributes', 'comment', 'action'])
                writer.writeheader()
                writer.writerows(self.results['orphaned_networks'])
            csv_files.append({'name': 'Orphaned AWS Networks', 'filename': filename})
        
        # 2. Conflicts CSV
        if self.results['conflicts']:
            filename = 'network_conflicts.csv'
            filepath = os.path.join(self.report_dir, filename)
            with open(filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['network1', 'network2', 'existing_source', 'type', 'severity', 'existing_network'])
                writer.writeheader()
                writer.writerows(self.results['conflicts'])
            csv_files.append({'name': 'Network Conflicts', 'filename': filename})
        
        # 3. Tag Discrepancies CSV
        if self.results['tag_discrepancies']:
            filename = 'tag_discrepancies.csv'
            filepath = os.path.join(self.report_dir, filename)
            with open(filepath, 'w', newline='') as f:
                # Flatten the structure for CSV
                rows = []
                for disc in self.results['tag_discrepancies']:
                    row = {
                        'network': disc['network'],
                        'action': disc['action'],
                        'missing_tags': json.dumps(disc['missing_tags']),
                        'updated_tags': json.dumps(disc['updated_tags'])
                    }
                    rows.append(row)
                
                writer = csv.DictWriter(f, fieldnames=['network', 'action', 'missing_tags', 'updated_tags'])
                writer.writeheader()
                writer.writerows(rows)
            csv_files.append({'name': 'Tag Discrepancies', 'filename': filename})
        
        # 4. Proposed Networks CSV
        if self.results['proposed_networks']:
            filename = 'proposed_networks.csv'
            filepath = os.path.join(self.report_dir, filename)
            with open(filepath, 'w', newline='') as f:
                rows = []
                for idx, net in enumerate(self.results['proposed_networks'], 1):
                    row = {
                        'priority': idx,
                        'cidr': net['cidr'],
                        'type': net['type'],
                        'tags': json.dumps(net['tags'])
                    }
                    rows.append(row)
                
                writer = csv.DictWriter(f, fieldnames=['priority', 'cidr', 'type', 'tags'])
                writer.writeheader()
                writer.writerows(rows)
            csv_files.append({'name': 'Proposed Networks', 'filename': filename})
        
        # 5. Network Hierarchy CSV
        if self.results['hierarchy']:
            filename = 'network_hierarchy.csv'
            filepath = os.path.join(self.report_dir, filename)
            with open(filepath, 'w', newline='') as f:
                rows = []
                for container, children in self.results['hierarchy'].items():
                    for child in children:
                        rows.append({
                            'container': container,
                            'child_network': child
                        })
                
                writer = csv.DictWriter(f, fieldnames=['container', 'child_network'])
                writer.writeheader()
                writer.writerows(rows)
            csv_files.append({'name': 'Network Hierarchy', 'filename': filename})
        
        return csv_files


class InfoBloxClient:
    """InfoBlox API Client with enhanced error handling"""
    
    def __init__(self, grid_master: str, username: str, password: str):
        self.grid_master = grid_master
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (username, password)
        self.session.verify = False
        self.base_url = f"https://{grid_master}/wapi/v2.13.1"
    
    def get_all_networks(self, network_view: str) -> List[Dict]:
        """Get all networks and containers from InfoBlox"""
        all_objects = []
        
        # Get regular networks
        try:
            response = self.session.get(
                f"{self.base_url}/network",
                params={
                    'network_view': network_view,
                    '_return_fields': 'network,extattrs,comment',
                    '_max_results': 10000
                }
            )
            if response.status_code == 200:
                networks = response.json()
                for net in networks:
                    net['_type'] = 'network'
                all_objects.extend(networks)
        except Exception as e:
            logger.error(f"Error fetching networks: {e}")
        
        # Get network containers
        try:
            response = self.session.get(
                f"{self.base_url}/networkcontainer",
                params={
                    'network_view': network_view,
                    '_return_fields': 'network,extattrs,comment',
                    '_max_results': 10000
                }
            )
            if response.status_code == 200:
                containers = response.json()
                for cont in containers:
                    cont['_type'] = 'networkcontainer'
                all_objects.extend(containers)
        except Exception as e:
            logger.error(f"Error fetching containers: {e}")
        
        return all_objects


def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Comprehensive InfoBlox vs AWS Network Analyzer'
    )
    parser.add_argument(
        'aws_csv', 
        help='Path to AWS export CSV file'
    )
    parser.add_argument(
        '--network-view', 
        help='InfoBlox network view to analyze',
        default=None
    )
    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Only generate report, do not make any changes'
    )
    return parser.parse_args()


def load_aws_data(csv_file: str) -> List[Dict]:
    """Load and parse AWS network data from CSV"""
    try:
        df = pd.read_csv(csv_file)
        networks = []
        
        for _, row in df.iterrows():
            # Find CIDR column
            cidr = row.get('cidr', row.get('CIDR', row.get('CidrBlock', row.get('network'))))
            if not cidr:
                logger.warning(f"No CIDR found in row: {row}")
                continue
                
            network = {
                'cidr': cidr,
                'tags': {}
            }
            
            # Parse tags from Tags column if it exists
            if 'Tags' in row and pd.notna(row['Tags']):
                try:
                    # Parse the tag list
                    tag_list = eval(row['Tags']) if isinstance(row['Tags'], str) else row['Tags']
                    # Convert list of dicts to single dict
                    for tag in tag_list:
                        if isinstance(tag, dict) and 'Key' in tag and 'Value' in tag:
                            network['tags'][tag['Key']] = tag['Value']
                except Exception as e:
                    logger.warning(f"Error parsing tags: {e}")
            
            # Add specific columns as tags
            tag_columns = ['Name', 'environment', 'owner', 'project', 'location', 'Description']
            for col in tag_columns:
                if col in row and pd.notna(row[col]):
                    network['tags'][col] = str(row[col])
            
            networks.append(network)
        
        return networks
    except Exception as e:
        logger.error(f"Error loading AWS data: {e}")
        raise


def main():
    """Main execution function"""
    load_dotenv('config.env')
    args = parse_arguments()
    
    # Get configuration
    grid_master = os.getenv('GRID_MASTER', 'infoblox.example.com')
    username = os.getenv('INFOBLOX_USERNAME') or input("InfoBlox username: ")
    password = os.getenv('INFOBLOX_PASSWORD') or os.getenv('PASSWORD') or getpass.getpass("InfoBlox password: ")
    network_view = args.network_view or os.getenv('NETWORK_VIEW', 'default')
    
    try:
        # Initialize InfoBlox client
        ib_client = InfoBloxClient(grid_master, username, password)
        
        # Load AWS data
        logger.info(f"Loading AWS data from {args.aws_csv}")
        aws_networks = load_aws_data(args.aws_csv)
        logger.info(f"Loaded {len(aws_networks)} networks from AWS export")
        
        # Get all InfoBlox networks
        logger.info(f"Fetching networks from InfoBlox view: {network_view}")
        infoblox_networks = ib_client.get_all_networks(network_view)
        logger.info(f"Found {len(infoblox_networks)} networks/containers in InfoBlox")
        
        # Perform analysis
        analyzer = NetworkAnalyzer(ib_client, network_view)
        results = analyzer.analyze_networks(aws_networks, infoblox_networks)
        
        # Generate report
        report_gen = ReportGenerator(results)
        report_path = report_gen.generate_full_report()
        
        print(f"\n✅ Analysis complete!")
        print(f"📊 Report generated: {report_path}")
        print(f"\n📋 Summary:")
        print(f"   - Orphaned networks: {len(results['orphaned_networks'])}")
        print(f"   - Conflicts found: {len(results['conflicts'])}")
        print(f"   - Tag discrepancies: {len(results['tag_discrepancies'])}")
        print(f"   - Proposed containers: {len([n for n in results['proposed_networks'] if n['type'] == 'CONTAINER'])}")
        print(f"   - Proposed networks: {len([n for n in results['proposed_networks'] if n['type'] == 'NETWORK'])}")
        
        if results['conflicts']:
            print("\n⚠️  CRITICAL: Network conflicts detected! Review report before proceeding.")
        
        if not args.report_only and results['proposed_networks']:
            response = input("\n🔄 Would you like to proceed with network creation? (yes/no): ")
            if response.lower() == 'yes':
                print("Network creation functionality would be implemented here...")
                # TODO: Implement network creation logic
        
    except Exception as e:
        logger.error(f"Error during analysis: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())