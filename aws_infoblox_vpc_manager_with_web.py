#!/usr/bin/env python3
"""
Enhanced AWS InfoBlox VPC Manager with Dynamic Tag Mapping Support

This is a modified version of aws_infoblox_vpc_manager_complete.py that reads
tag mappings from the tag_mappings.json file created by the web interface.
"""

import json
import os
from typing import Dict

# Import everything from the original script
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from aws_infoblox_vpc_manager_complete import *

# Override the VPCManager class to use dynamic mappings
class EnhancedVPCManager(VPCManager):
    """Enhanced VPC Manager that uses dynamic tag mappings"""
    
    def __init__(self, infoblox_client: InfoBloxClient):
        super().__init__(infoblox_client)
        self.tag_mappings = self.load_tag_mappings()
        
    def load_tag_mappings(self) -> Dict[str, str]:
        """Load tag mappings from JSON file"""
        mappings_file = 'tag_mappings.json'
        
        # Default mappings
        default_mappings = {
            'Name': 'aws_name',
            'environment': 'environment',
            'Environment': 'environment',
            'owner': 'owner',
            'Owner': 'owner',
            'project': 'project',
            'Project': 'project',
            'location': 'aws_location',
            'Location': 'aws_location',
            'cloudservice': 'aws_cloudservice',
            'createdby': 'aws_created_by',
            'RequestedBy': 'aws_requested_by',
            'Requested_By': 'aws_requested_by',
            'dud': 'aws_dud',
            'AccountId': 'aws_account_id',
            'Region': 'aws_region',
            'VpcId': 'aws_vpc_id',
            'Description': 'description'
        }
        
        if os.path.exists(mappings_file):
            try:
                with open(mappings_file, 'r') as f:
                    custom_mappings = json.load(f)
                    logger.info(f"Loaded {len(custom_mappings)} tag mappings from {mappings_file}")
                    return custom_mappings
            except Exception as e:
                logger.warning(f"Error loading tag mappings from {mappings_file}: {e}")
                logger.info("Using default tag mappings")
        else:
            logger.info("No custom tag mappings file found, using defaults")
        
        return default_mappings
    
    def map_aws_tags_to_infoblox_eas(self, aws_tags: Dict[str, str]) -> Dict[str, str]:
        """Map AWS tags to InfoBlox Extended Attributes using dynamic mappings"""
        mapped_eas = {}
        
        for aws_key, aws_value in aws_tags.items():
            # Check if we have a mapping for this tag
            if aws_key in self.tag_mappings:
                ea_key = self.tag_mappings[aws_key]
            else:
                # If no mapping exists, create a default one
                ea_key = f"aws_{aws_key.lower()}"
                ea_key = ea_key.replace('-', '_').replace(' ', '_').lower()
                logger.debug(f"No mapping found for AWS tag '{aws_key}', using default: '{ea_key}'")
            
            # Ensure EA value doesn't exceed InfoBlox limit
            ea_value = str(aws_value)[:255] if len(str(aws_value)) > 255 else str(aws_value)
            mapped_eas[ea_key] = ea_value
        
        return mapped_eas

# Override the main function to use the enhanced VPC manager
def enhanced_main():
    """Enhanced main function that uses dynamic tag mappings"""
    args = parse_arguments()
    
    try:
        config_override = None
        
        # Check if interactive mode is requested
        if args.interactive:
            # Show and optionally edit configuration
            config_override = show_and_edit_config()
        else:
            # Quiet mode - just load from config.env
            logger.info("Running in quiet mode. Use -i for interactive configuration.")
        
        # Get configuration (no prompting in quiet mode)
        grid_master, network_view, username, password, csv_file, container_prefixes, container_mode = get_config(
            config_override=config_override
        )
        
        # Override network view if specified on command line
        if args.network_view:
            network_view = args.network_view
            print(f"Using network view from command line: {network_view}")
            
        # Override CSV file if specified on command line
        if args.csv_file and args.csv_file != 'vpc_data.csv':
            csv_file = args.csv_file
            print(f"Using CSV file from command line: {csv_file}")
        
        # Show container configuration
        if container_prefixes:
            print(f"📦 Container prefixes configured: /{', /'.join(map(str, container_prefixes))}")
            print(f"🔧 Container mode: {container_mode}")
        else:
            print("📦 Container detection: Auto-detect from InfoBlox")
        
        # Show tag mapping info
        print("\n🏷️  Tag Mapping Configuration:")
        if os.path.exists('tag_mappings.json'):
            print("   ✅ Using custom tag mappings from tag_mappings.json")
            print("   💡 Run the web interface (python tag_mapping_web_app.py) to modify mappings")
        else:
            print("   ℹ️  Using default tag mappings")
            print("   💡 Run the web interface (python tag_mapping_web_app.py) to create custom mappings")
        
        logger.info(f"Loading VPC data from {csv_file}...")
        
        # Initialize InfoBlox client
        print(f"\n🔗 Connecting to InfoBlox Grid Master: {grid_master}")
        ib_client = InfoBloxClient(grid_master, username, password)
        
        # Initialize Enhanced VPC Manager
        vpc_manager = EnhancedVPCManager(ib_client)
        
        # Load and parse VPC data
        try:
            vpc_df = vpc_manager.load_vpc_data(csv_file)
            vpc_df = vpc_manager.parse_vpc_tags(vpc_df)
        except Exception as e:
            logger.error(f"Failed to load VPC data: {e}")
            return 1
        
        print(f"\n📊 ANALYSIS SUMMARY:")
        print(f"   📁 CSV file: {csv_file}")
        print(f"   🔢 Total VPCs loaded: {len(vpc_df)}")
        print(f"   🌐 Network view: {network_view}")
        
        # Compare with InfoBlox
        logger.info("Comparing AWS VPCs with InfoBlox networks...")
        comparison_results = vpc_manager.compare_vpc_with_infoblox(vpc_df, network_view)
        
        # Display results
        print(f"\n🔍 COMPARISON RESULTS:")
        print(f"   ✅ Fully synchronized (network + tags): {len(comparison_results['matches'])}")
        print(f"   🔴 Missing from InfoBlox: {len(comparison_results['missing'])}")
        print(f"   🟡 Networks with outdated tags: {len(comparison_results['discrepancies'])}")
        print(f"   📦 Network containers: {len(comparison_results['containers'])}")
        print(f"   ❌ Processing errors: {len(comparison_results['errors'])}")
        
        # Show update requirements summary
        if comparison_results['discrepancies']:
            print(f"\n🔧 UPDATE REQUIREMENTS:")
            print(f"   🏷️ Networks requiring EA updates: {len(comparison_results['discrepancies'])}")
            
            # Show sample of networks that need updates
            sample_discrepancies = comparison_results['discrepancies'][:3]
            for item in sample_discrepancies:
                vpc_name = item['vpc'].get('Name', 'Unnamed')
                cidr = item['cidr']
                print(f"   📄 {cidr} ({vpc_name}) - EAs need updating")
            
            if len(comparison_results['discrepancies']) > 3:
                print(f"   ... and {len(comparison_results['discrepancies']) - 3} more networks")
        
        # Show network containers summary
        if comparison_results.get('containers'):
            print(f"\n📦 NETWORK CONTAINERS FOUND:")
            print(f"   🔢 VPCs existing as containers: {len(comparison_results['containers'])}")
            print(f"   ℹ️ These exist as network containers (parent networks) in InfoBlox")
            print(f"   💡 Container networks typically contain smaller subnet networks")
            for container in comparison_results['containers'][:3]:
                print(f"   📦 {container['cidr']} - {container['vpc']['Name']}")
            if len(comparison_results['containers']) > 3:
                print(f"   ... and {len(comparison_results['containers']) - 3} more")
        
        # Analyze Extended Attributes (regardless of missing networks)
        if args.create_missing:
            print(f"\n🔍 EXTENDED ATTRIBUTES ANALYSIS:")
            ea_analysis = vpc_manager.ensure_required_eas(vpc_df, dry_run=args.dry_run)
            
            # Generate EA summary report
            reports_dir = "reports"
            os.makedirs(reports_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ea_report_filename = os.path.join(reports_dir, f"extended_attributes_summary_{timestamp}.txt")
            
            eas_to_report = []
            report_ea_title = ""

            if args.dry_run:
                print(f"   🏷️ Extended Attributes analysis: {len(ea_analysis['missing_eas'])} missing")
                eas_to_report = ea_analysis.get('missing_eas', [])
                report_ea_title = "Missing Extended Attributes (would be created):"
            else:
                print(f"   🏷️ Extended Attributes: {ea_analysis['created_count']} created, {ea_analysis['existing_count']} existed")
                created_eas = [name for name, status in ea_analysis.get('ea_results', {}).items() if status == 'created']
                eas_to_report = created_eas
                report_ea_title = "Extended Attributes Created:"

            if eas_to_report:
                with open(ea_report_filename, 'w', encoding='utf-8') as f:
                    f.write(f"{report_ea_title}\n")
                    f.write("=" * len(report_ea_title) + "\n")
                    for ea_name in eas_to_report:
                        f.write(f"{ea_name}\n")
                logger.info(f"Generated Extended Attributes summary: {ea_report_filename}")
                print(f"   📄 Extended Attributes summary file: {ea_report_filename}")
            else:
                logger.info("No new or missing Extended Attributes to report.")

        # Handle create-missing flag for networks
        if args.create_missing and comparison_results['missing']:
            print(f"\n🚀 CREATING MISSING NETWORKS:")
            
            # Sort missing networks by priority (larger networks first)
            missing_with_priority = []
            for item in comparison_results['missing']:
                vpc = item['vpc']
                aws_tags = item['aws_tags']
                priority = vpc_manager._calculate_network_priority(vpc, aws_tags)
                missing_with_priority.append((priority, item))
            
            # Sort by priority
            missing_with_priority.sort(key=lambda x: x[0])
            sorted_missing = [item for priority, item in missing_with_priority]
            
            print(f"   📋 Creating {len(sorted_missing)} networks in priority order...")
            print(f"   🔢 Priority order: larger networks (/16, /17) before smaller (/24, /25)")
            
            # Create networks
            operation_results = vpc_manager.create_missing_networks(
                sorted_missing, 
                network_view=network_view, 
                dry_run=args.dry_run
            )
            
            # Show results
            created_count = sum(1 for r in operation_results if r.get('action') == 'created')
            would_create_count = sum(1 for r in operation_results if r.get('action') == 'would_create')
            error_count = sum(1 for r in operation_results if r.get('action') == 'error')
            rejected_count = sum(1 for r in operation_results if r.get('action') == 'would_reject')
            
            if args.dry_run:
                print(f"   ✅ Would create: {would_create_count}")
                print(f"   ⚠️ Would reject: {rejected_count}")
                print(f"   ❌ Would fail: {error_count}")
            else:
                print(f"   ✅ Successfully created: {created_count}")
                print(f"   ❌ Failed to create: {error_count}")
                if error_count > 0:
                    print(f"   📄 Check rejected networks CSV for failed creations")
        
        # Handle EA Discrepancies
        if args.create_missing and comparison_results['discrepancies']:
            print(f"\n🔧 FIXING EA DISCREPANCIES:")
            discrepancy_results = vpc_manager.fix_ea_discrepancies(
                comparison_results['discrepancies'], 
                dry_run=args.dry_run
            )
            
            if args.dry_run:
                print(f"   🔧 Would update {discrepancy_results['would_update_count']} networks with correct EAs")
            else:
                print(f"   ✅ Updated {discrepancy_results['updated_count']} networks")
                print(f"   ❌ Failed to update {discrepancy_results['failed_count']} networks")

        # Generate EA Discrepancies Report
        if comparison_results['discrepancies']:
            generate_ea_discrepancies_report(comparison_results['discrepancies'])
        
        # Generate Comprehensive Network Status Report
        generate_network_status_report(comparison_results, args.dry_run)

        print(f"\n✅ OPERATION COMPLETED")
        print(f"   📝 Check logs: aws_infoblox_vpc_manager.log")
        print(f"   📊 For detailed reports, check the reports/ directory")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n⚠️ Operation cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(enhanced_main())