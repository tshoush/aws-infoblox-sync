#!/usr/bin/env python3
"""
Mock InfoBlox data representing existing networks from multiple sources
This simulates what would be returned from InfoBlox API
"""

mock_infoblox_networks = [
    # AWS Networks already in InfoBlox
    {
        'network': '10.60.0.0/24',  # This AWS network is NOT in the new export (orphaned)
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'Environment': {'value': 'Production'},
            'Status': {'value': 'Deprecated'}
        },
        'comment': 'Old AWS production VPC - scheduled for decommission'
    },
    {
        'network': '10.70.0.0/24',  # This AWS network IS in the export but missing tags
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'Environment': {'value': 'Production'},  # Missing 'NewTag' from CSV
            'Team': {'value': 'CorePlatform'}
        },
        'comment': 'Existing AWS production network'
    },
    
    # Azure Networks
    {
        'network': '172.16.0.0/16',  # Azure container that contains AWS 172.16.0.0/24
        '_type': 'networkcontainer',
        'extattrs': {
            'Source': {'value': 'Azure'},
            'Environment': {'value': 'Production'},
            'Subscription': {'value': 'Azure-Prod-001'}
        },
        'comment': 'Azure production VNET'
    },
    {
        'network': '172.16.1.0/24',  # Azure subnet inside the container
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'Azure'},
            'Environment': {'value': 'Production'}
        },
        'comment': 'Azure subnet 1'
    },
    
    # GCP Networks
    {
        'network': '10.50.1.0/24',  # GCP network that partially overlaps with AWS 10.50.0.0/23
        '_type': 'network',
        'extattrs': {
            'Cloud_Provider': {'value': 'GCP'},
            'Project': {'value': 'gcp-shared-services'},
            'Environment': {'value': 'Production'}
        },
        'comment': 'GCP shared services network'
    },
    
    # On-Premises Networks
    {
        'network': '192.168.1.0/24',  # Same as AWS EU network (exact match conflict)
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'OnPrem'},
            'Location': {'value': 'EU-Datacenter-1'},
            'VLAN': {'value': '100'}
        },
        'comment': 'On-premises datacenter network in EU'
    },
    {
        'network': '10.80.0.0/16',  # On-prem container that contains AWS 10.80.5.128/25
        '_type': 'network',  # Note: This is a regular network, not a container!
        'extattrs': {
            'Source': {'value': 'OnPrem'},
            'Location': {'value': 'US-Datacenter-2'},
            'Purpose': {'value': 'Legacy Infrastructure'}
        },
        'comment': 'Legacy on-prem network acting as non-container'
    },
    
    # Other cloud provider
    {
        'network': '10.200.0.0/20',  # Contains part of AWS dev network
        '_type': 'networkcontainer',
        'extattrs': {
            'Source': {'value': 'OCI'},
            'Environment': {'value': 'Development'},
            'Region': {'value': 'us-phoenix-1'}
        },
        'comment': 'Oracle Cloud Infrastructure development'
    },
    
    # Network without source (ambiguous)
    {
        'network': '10.30.0.0/24',
        '_type': 'network',
        'extattrs': {
            'Environment': {'value': 'Test'}
            # No Source or Cloud_Provider tag
        },
        'comment': 'Test network - source unknown'
    },
    
    # AWS network from different account/region not in this export
    {
        'network': '10.40.0.0/23',
        '_type': 'network',
        'extattrs': {
            'Source': {'value': 'AWS'},
            'AWSAccount': {'value': '999999999999'},
            'Region': {'value': 'ap-southeast-1'},
            'Environment': {'value': 'Production'}
        },
        'comment': 'AWS network from different account - not in this export'
    }
]

def get_mock_infoblox_data():
    """Return mock InfoBlox data for testing"""
    return mock_infoblox_networks

if __name__ == "__main__":
    import json
    print("Mock InfoBlox Networks:")
    print(json.dumps(mock_infoblox_networks, indent=2))