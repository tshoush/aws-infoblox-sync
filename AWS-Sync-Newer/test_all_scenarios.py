#!/usr/bin/env python3
"""
Comprehensive test of all AWS-InfoBlox synchronization scenarios
Demonstrates all use cases with the test CSV data
"""

import json
import sys
from datetime import datetime
from infoblox_aws_comprehensive_analyzer import NetworkAnalyzer, ReportGenerator, load_aws_data
from mock_infoblox_data import get_mock_infoblox_data

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def run_comprehensive_test():
    """Run comprehensive test with all use cases"""
    print("🚀 AWS-InfoBlox Comprehensive Use Case Test")
    print(f"   Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load test data
    print_section("1. Loading Test Data")
    
    # Load AWS data from CSV
    try:
        aws_networks = load_aws_data('test_all_use_cases.csv')
        print(f"✅ Loaded {len(aws_networks)} AWS networks from CSV")
        
        # Show sample
        print("\nSample AWS networks:")
        for i, net in enumerate(aws_networks[:3]):
            print(f"   {i+1}. {net['cidr']} - {net['tags'].get('Name', 'Unnamed')}")
            print(f"      Description: {net['tags'].get('Description', 'None')}")
    except Exception as e:
        print(f"❌ Error loading AWS data: {e}")
        return
    
    # Get mock InfoBlox data
    infoblox_networks = get_mock_infoblox_data()
    print(f"\n✅ Loaded {len(infoblox_networks)} existing networks from InfoBlox")
    print("\nInfoBlox network sources:")
    sources = {}
    for net in infoblox_networks:
        source = (net.get('extattrs', {}).get('Source', {}).get('value') or 
                 net.get('extattrs', {}).get('Cloud_Provider', {}).get('value') or 
                 'Unknown')
        sources[source] = sources.get(source, 0) + 1
    for source, count in sources.items():
        print(f"   - {source}: {count} networks")
    
    # Run analysis
    print_section("2. Running Network Analysis")
    
    analyzer = NetworkAnalyzer(None, 'Production')
    results = analyzer.analyze_networks(aws_networks, infoblox_networks)
    
    # Display detailed results
    print_section("3. Analysis Results - Use Cases Demonstrated")
    
    # Use Case 1: Orphaned AWS Networks
    print("📌 Use Case 1: Orphaned AWS Networks")
    print("   (AWS networks in InfoBlox but not in current export)")
    if results['orphaned_networks']:
        for net in results['orphaned_networks']:
            print(f"   ❗ {net['network']} - {net.get('comment', 'No comment')}")
            print(f"      Source: {net['source']}, Action: {net['action']}")
    else:
        print("   ✅ No orphaned AWS networks found")
    
    # Use Case 2: Network Conflicts
    print("\n📌 Use Case 2: Network Conflicts (All Types)")
    if results['conflicts']:
        conflict_types = {}
        for conflict in results['conflicts']:
            ctype = conflict['type']
            conflict_types[ctype] = conflict_types.get(ctype, [])
            conflict_types[ctype].append(conflict)
        
        for ctype, conflicts in conflict_types.items():
            print(f"\n   Conflict Type: {ctype}")
            for c in conflicts:
                print(f"   ⚠️  AWS {c['network1']} ↔️ {c['network2']} (Source: {c.get('existing_source', 'Unknown')})")
                print(f"      Severity: {c['severity']}")
    else:
        print("   ✅ No conflicts found")
    
    # Use Case 3: Hierarchical Networks (Containers)
    print("\n📌 Use Case 3: Hierarchical Network Management")
    print("   (Networks that should be created as containers)")
    
    # Show hierarchy
    if results['hierarchy']:
        print("\n   Network Hierarchy:")
        for container, children in results['hierarchy'].items():
            print(f"   📦 {container} (Container)")
            for child in children:
                print(f"      └── {child}")
    
    # Show proposed containers
    if results['proposed_containers']:
        print("\n   Proposed Containers (due to existing children):")
        for pc in results['proposed_containers']:
            print(f"   📦 {pc['cidr']} - {pc['reason']}")
            if 'contained_networks' in pc:
                for cn in pc['contained_networks']:
                    if isinstance(cn, dict):
                        print(f"      └── {cn['network']} (Source: {cn['source']})")
                    else:
                        print(f"      └── {cn}")
    
    # Use Case 4: Tag Management
    print("\n📌 Use Case 4: Tag Preservation & Updates")
    print("   (AWS networks with missing or changed tags)")
    if results['tag_discrepancies']:
        for disc in results['tag_discrepancies']:
            print(f"\n   🏷️  Network: {disc['network']} (Current source: {disc['current_source']})")
            if disc['missing_tags']:
                print(f"      Missing tags: {list(disc['missing_tags'].keys())}")
            if disc['updated_tags']:
                print("      Changed tags:")
                for tag, values in disc['updated_tags'].items():
                    print(f"         {tag}: '{values['old_value']}' → '{values['new_value']}'")
    else:
        print("   ✅ All tags are synchronized")
    
    # Use Case 5: New Network Creation
    print("\n📌 Use Case 5: New Network Creation Order")
    print("   (Networks to be created, sorted by priority)")
    
    containers = [n for n in results['proposed_networks'] if n['type'] == 'CONTAINER']
    networks = [n for n in results['proposed_networks'] if n['type'] == 'NETWORK']
    
    if containers:
        print(f"\n   Containers to create ({len(containers)}):")
        for i, cont in enumerate(containers[:5]):
            print(f"   {i+1}. {cont['cidr']} - {cont['tags'].get('Name', 'Unnamed')}")
    
    if networks:
        print(f"\n   Networks to create ({len(networks)}):")
        for i, net in enumerate(networks[:5]):
            print(f"   {i+1}. {net['cidr']} - {net['tags'].get('Name', 'Unnamed')}")
    
    # Summary statistics
    print_section("4. Summary Statistics")
    print(f"📊 Analysis Summary:")
    print(f"   - Total AWS networks in export: {len(aws_networks)}")
    print(f"   - Total networks in InfoBlox: {len(infoblox_networks)}")
    print(f"   - Orphaned AWS networks: {len(results['orphaned_networks'])}")
    print(f"   - Conflicts detected: {len(results['conflicts'])}")
    print(f"   - Tag discrepancies: {len(results['tag_discrepancies'])}")
    print(f"   - Proposed containers: {len(containers)}")
    print(f"   - Proposed networks: {len(networks)}")
    
    # Generate report
    print_section("5. Generating Reports")
    report_gen = ReportGenerator(results)
    report_path = report_gen.generate_full_report()
    print(f"✅ HTML report generated: {report_path}")
    
    # Save test results
    test_results = {
        'test_timestamp': datetime.now().isoformat(),
        'aws_networks_count': len(aws_networks),
        'infoblox_networks_count': len(infoblox_networks),
        'analysis_results': results,
        'use_cases_tested': [
            'Orphaned AWS networks detection',
            'Multi-source conflict detection',
            'Hierarchical container management',
            'Tag preservation and updates',
            'Priority-based network creation'
        ]
    }
    
    import os
    results_file = os.path.join(os.path.dirname(report_path), 'test_results.json')
    with open(results_file, 'w') as f:
        json.dump(test_results, f, indent=2, default=str)
    print(f"✅ Test results saved: {results_file}")
    
    print("\n✨ All use cases successfully demonstrated!")
    print("\nNext steps:")
    print("1. Review the HTML report for detailed analysis")
    print("2. Check CSV files for bulk operations")
    print("3. Use the network updater to apply changes")
    
    return results

if __name__ == "__main__":
    results = run_comprehensive_test()