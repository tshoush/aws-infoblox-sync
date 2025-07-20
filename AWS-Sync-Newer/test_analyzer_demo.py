#!/usr/bin/env python3
"""
Demo script to show the analyzer functionality with mock data
"""

import json
import os
from datetime import datetime
from infoblox_aws_comprehensive_analyzer import NetworkAnalyzer, ReportGenerator

# Create mock InfoBlox data representing a multi-source environment
mock_infoblox_networks = [
    # AWS networks (will be checked for orphans)
    {
        'network': '10.212.226.0/23',
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'Environment': {'value': 'Production'}
        },
        'comment': 'AWS VPC - DevOps shared services'
    },
    {
        'network': '10.100.0.0/16',  # AWS network not in current export (orphaned)
        '_type': 'networkcontainer',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'Region': {'value': 'us-west-2'}
        },
        'comment': 'Old AWS VPC - deprecated'
    },
    
    # Azure networks
    {
        'network': '10.212.230.0/24',  # Will conflict with AWS 10.212.230.0/23
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'Azure'},
            'Environment': {'value': 'Production'}
        },
        'comment': 'Azure VNET - MPG Platform'
    },
    
    # GCP networks
    {
        'network': '15.212.0.0/16',  # Contains AWS network 15.212.224.0/23
        '_type': 'networkcontainer',
        'extattrs': {
            'Cloud_Provider': {'value': 'GCP'},
            'Project': {'value': 'Analytics'}
        },
        'comment': 'GCP VPC for Analytics workloads'
    },
    
    # On-premises networks
    {
        'network': '10.212.19.0/24',  # Will partially overlap with AWS 10.212.19.128/25
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'OnPrem'},
            'Location': {'value': 'Datacenter-1'}
        },
        'comment': 'On-premises datacenter network'
    },
    
    # AWS network with wrong tags
    {
        'network': '12.212.88.0/24',
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'Environment': {'value': 'dev'}  # Should be 'test' per CSV
        },
        'comment': 'AWS VPC - Finance test'
    }
]

# Mock AWS networks from CSV
mock_aws_networks = [
    {
        'cidr': '15.212.224.0/23',
        'tags': {
            'Name': 'mi-lz-icd-core-team-hold-prod-pci-us-east-1-vpc',
            'Environment': 'prodpci',
            'Owner': 'S:Public Cloud Adnan Haq',
            'Project': 'Backup Account in AWS'
        }
    },
    {
        'cidr': '12.216.140.0/23',
        'tags': {
            'Name': 'mi-lz-icd-core-team-hold-prod-pci-us-west-2-vpc',
            'Environment': 'prodpci',
            'Location': 'aws-us-west-2'
        }
    },
    {
        'cidr': '12.212.88.0/24',
        'tags': {
            'Name': 'mi-lz-dc-finance-test-us-east-1-vpc',
            'Environment': 'test',
            'Owner': 'I:MGP Impacted Sys Fin Sanchita Sarkar'
        }
    },
    {
        'cidr': '15.212.118.0/25',
        'tags': {
            'Name': 'mi-lz-tech-svcs-dev-us-east-1-vpc',
            'Environment': 'Dev',
            'Project': 'Tech Services'
        }
    },
    {
        'cidr': '10.212.226.0/23',
        'tags': {
            'Name': 'mi-lz-devops-ss-us-east-1-vpc',
            'Environment': 'shared services',
            'Owner': 'H:Infra Engineering param_value Auto Adnan Haq'
        }
    },
    {
        'cidr': '10.212.230.0/23',
        'tags': {
            'Name': 'mi-lz-mpg-prod-us-east-1-vpc',
            'Environment': 'prod',
            'Owner': 'Jesus Lopez'
        }
    },
    {
        'cidr': '10.212.19.128/25',
        'tags': {
            'Name': 'mi-lz-network-test-default',
            'Environment': 'test'
        }
    }
]

def run_demo():
    """Run the demo analysis"""
    print("🚀 AWS-InfoBlox Network Analyzer Demo")
    print("=" * 50)
    print("\n📊 Analyzing networks in multi-source environment...")
    print(f"   - AWS networks in export: {len(mock_aws_networks)}")
    print(f"   - Total networks in InfoBlox: {len(mock_infoblox_networks)}")
    print(f"   - Sources: AWS, Azure, GCP, OnPrem")
    
    # Create analyzer (mock client not needed for analysis)
    analyzer = NetworkAnalyzer(None, 'AWSTesting')
    
    # Run analysis
    results = analyzer.analyze_networks(mock_aws_networks, mock_infoblox_networks)
    
    print("\n✅ Analysis Complete!")
    print("\n📋 Summary:")
    print(f"   - Orphaned AWS networks: {len(results['orphaned_networks'])}")
    print(f"   - Conflicts detected: {len(results['conflicts'])}")
    print(f"   - Tag discrepancies: {len(results['tag_discrepancies'])}")
    print(f"   - Networks requiring containers: {len(results['proposed_containers'])}")
    print(f"   - New networks to create: {len(results['proposed_networks'])}")
    
    # Show details
    if results['orphaned_networks']:
        print("\n🔍 Orphaned AWS Networks:")
        for net in results['orphaned_networks']:
            print(f"   - {net['network']} ({net['source']})")
    
    if results['conflicts']:
        print("\n⚠️  Conflicts Found:")
        for conflict in results['conflicts']:
            print(f"   - AWS {conflict['network1']} conflicts with {conflict['network2']} "
                  f"(Source: {conflict.get('existing_source', 'Unknown')}) "
                  f"- Type: {conflict['type']}")
    
    if results['tag_discrepancies']:
        print("\n🏷️  Tag Discrepancies:")
        for disc in results['tag_discrepancies']:
            print(f"   - {disc['network']}: {len(disc['missing_tags'])} missing, "
                  f"{len(disc['updated_tags'])} to update")
    
    # Generate report
    print("\n📊 Generating HTML report...")
    report_gen = ReportGenerator(results)
    report_path = report_gen.generate_full_report()
    print(f"✅ Report generated: {report_path}")
    
    # Save analysis results
    results_file = os.path.join(report_gen.report_dir, 'analysis_results.json')
    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"💾 Analysis results saved: {results_file}")
    
    print("\n🎯 Next Steps:")
    print("1. Review the HTML report for detailed analysis")
    print("2. Resolve any conflicts before proceeding")
    print("3. Use infoblox_aws_network_updater.py to apply changes")
    
    return results

if __name__ == "__main__":
    results = run_demo()