#!/usr/bin/env python3
"""
Run comprehensive test against actual InfoBlox with all use case scenarios
"""

import os
import sys
import subprocess
from datetime import datetime

def print_banner(text):
    """Print a formatted banner"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")

def main():
    """Run the comprehensive test against real InfoBlox"""
    print("🚀 AWS-InfoBlox Comprehensive Test - All Use Cases")
    print(f"   Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   InfoBlox: {os.getenv('GRID_MASTER', 'Not configured')}")
    print(f"   Network View: {os.getenv('NETWORK_VIEW', 'AWSTesting')}")
    
    # Ensure we have the test CSV
    if not os.path.exists('test_all_use_cases.csv'):
        print("❌ Error: test_all_use_cases.csv not found!")
        print("   This file contains all test scenarios.")
        return 1
    
    print_banner("Test Scenarios in CSV")
    print("The test CSV includes:")
    print("✓ Hierarchical networks (/16 → /24 → /25)")
    print("✓ Networks that will conflict with Azure/GCP/On-prem")
    print("✓ Networks with additional CIDR blocks")
    print("✓ Networks with various tags and metadata")
    print("✓ Networks that simulate all conflict types")
    
    print_banner("Running Analysis")
    print("Analyzing test_all_use_cases.csv against InfoBlox...")
    
    # Run the analyzer
    cmd = [
        sys.executable,
        'infoblox_aws_comprehensive_analyzer.py',
        'test_all_use_cases.csv',
        '--network-view', os.getenv('NETWORK_VIEW', 'AWSTesting')
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Analysis completed successfully!")
            
            # Extract key information from output
            output_lines = result.stdout.split('\n')
            for line in output_lines:
                if 'Report generated:' in line:
                    report_path = line.split('Report generated:')[1].strip()
                    print(f"\n📊 Report: {report_path}")
                elif 'Orphaned networks:' in line:
                    print(f"   {line.strip()}")
                elif 'Conflicts found:' in line:
                    print(f"   {line.strip()}")
                elif 'Tag discrepancies:' in line:
                    print(f"   {line.strip()}")
                elif 'Proposed containers:' in line:
                    print(f"   {line.strip()}")
                elif 'Proposed networks:' in line:
                    print(f"   {line.strip()}")
            
            print_banner("Expected Results")
            print("Based on the test data, you should see:")
            print("")
            print("1. HIERARCHICAL STRUCTURES:")
            print("   - 10.100.0.0/16 → Container (contains /24 and /25 networks)")
            print("   - 10.200.0.0/16 → Container (contains /24 networks)")
            print("   - 10.90.0.0/16 → Container (sandbox with child networks)")
            print("")
            print("2. CONFLICTS (if these exist in InfoBlox):")
            print("   - 172.16.0.0/24 vs Azure 172.16.0.0/16")
            print("   - 10.50.0.0/23 vs GCP 10.50.1.0/24")
            print("   - 192.168.1.0/24 vs On-prem (exact match)")
            print("   - 10.80.5.128/25 contained by On-prem 10.80.0.0/16")
            print("")
            print("3. TAG MANAGEMENT:")
            print("   - All networks get 'Source: AWS' tag")
            print("   - Existing AWS networks get tag updates")
            print("   - Non-AWS networks remain untouched")
            print("")
            print("4. ORPHAN DETECTION:")
            print("   - Only AWS-sourced networks not in export")
            print("   - Non-AWS networks ignored")
            
            print_banner("Next Steps")
            print("1. Review the HTML report for detailed analysis")
            print("2. Check CSV files in the report directory:")
            print("   - proposed_networks.csv")
            print("   - network_conflicts.csv (if any)")
            print("   - orphaned_aws_networks.csv (if any)")
            print("   - tag_discrepancies.csv (if any)")
            print("3. To apply changes (dry-run first):")
            print(f"   python infoblox_aws_network_updater.py [report_dir]/analysis_results.json --dry-run")
            
        else:
            print("❌ Analysis failed!")
            print("Error output:")
            print(result.stderr)
            return 1
            
    except Exception as e:
        print(f"❌ Error running analyzer: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())