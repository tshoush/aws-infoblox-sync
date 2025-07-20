#!/usr/bin/env python3
"""
AWS to InfoBlox Tag Mapping Web Interface
Provides a web-based UI for managing tag mappings between AWS and InfoBlox Extended Attributes
"""

from flask import Flask, render_template, request, jsonify, send_from_directory, Response
import json
import os
import pandas as pd
from typing import Dict, List, Optional, Tuple
import logging
from datetime import datetime
import sys
import requests
from urllib3.exceptions import InsecureRequestWarning
import time
from queue import Queue
import threading

# Suppress SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Add the parent directory to the path to import the main script
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from aws_infoblox_vpc_manager_complete import InfoBloxClient, AWSTagParser, VPCManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# File to store custom mappings
# Check if running in Docker and adjust path accordingly
if os.path.exists('/app/data'):
    MAPPINGS_FILE = '/app/data/tag_mappings.json'
else:
    MAPPINGS_FILE = 'tag_mappings.json'
DEFAULT_MAPPINGS = {
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

class TagMappingManager:
    """Manages AWS to InfoBlox tag mappings"""
    
    def __init__(self):
        self.mappings = self.load_mappings()
        self.infoblox_client = None
        
    def load_mappings(self) -> Dict[str, str]:
        """Load mappings from file or return defaults"""
        if os.path.exists(MAPPINGS_FILE):
            try:
                with open(MAPPINGS_FILE, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Error loading mappings: {e}")
        return DEFAULT_MAPPINGS.copy()
    
    def save_mappings(self, mappings: Dict[str, str]) -> bool:
        """Save mappings to file"""
        try:
            with open(MAPPINGS_FILE, 'w') as f:
                json.dump(mappings, f, indent=2)
            self.mappings = mappings
            return True
        except Exception as e:
            logger.error(f"Error saving mappings: {e}")
            return False
    
    def get_aws_tags_from_csv(self, csv_file: str = 'vpc_data.csv') -> List[str]:
        """Extract unique AWS tags from CSV file"""
        try:
            if not os.path.exists(csv_file):
                return []
            
            df = pd.read_csv(csv_file)
            if 'Tags' not in df.columns:
                return []
            
            parser = AWSTagParser()
            all_tags = set()
            
            for tags_str in df['Tags']:
                tags = parser.parse_tags_from_string(tags_str)
                all_tags.update(tags.keys())
            
            return sorted(list(all_tags))
        except Exception as e:
            logger.error(f"Error extracting AWS tags: {e}")
            return []
    
    def get_infoblox_eas(self) -> List[str]:
        """Get available InfoBlox Extended Attributes"""
        try:
            if not self.infoblox_client:
                self.connect_to_infoblox()
            
            if self.infoblox_client:
                eas = self.infoblox_client.get_extensible_attributes()
                return sorted([ea['name'] for ea in eas])
            return []
        except Exception as e:
            logger.error(f"Error fetching InfoBlox EAs: {e}")
            return []
    
    def connect_to_infoblox(self):
        """Connect to InfoBlox using config.env"""
        try:
            # Load configuration
            from dotenv import load_dotenv
            load_dotenv('config.env')
            
            grid_master = os.getenv('GRID_MASTER', '')
            username = os.getenv('INFOBLOX_USERNAME', '')
            password = os.getenv('PASSWORD', '')
            
            if grid_master and username and password:
                self.infoblox_client = InfoBloxClient(grid_master, username, password)
                logger.info("Connected to InfoBlox successfully")
            else:
                logger.warning("InfoBlox credentials not found in config.env")
        except Exception as e:
            logger.error(f"Error connecting to InfoBlox: {e}")
    
    def add_mapping(self, aws_tag: str, infoblox_ea: str) -> bool:
        """Add or update a mapping"""
        self.mappings[aws_tag] = infoblox_ea
        return self.save_mappings(self.mappings)
    
    def remove_mapping(self, aws_tag: str) -> bool:
        """Remove a mapping"""
        if aws_tag in self.mappings:
            del self.mappings[aws_tag]
            return self.save_mappings(self.mappings)
        return False
    
    def get_suggested_ea_name(self, aws_tag: str) -> str:
        """Suggest an EA name based on AWS tag"""
        # Convert to lowercase and replace special characters
        suggested = f"aws_{aws_tag.lower()}"
        suggested = suggested.replace('-', '_').replace(' ', '_')
        # Remove any non-alphanumeric characters except underscore
        suggested = ''.join(c for c in suggested if c.isalnum() or c == '_')
        return suggested

# Initialize the manager
mapping_manager = TagMappingManager()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'AWS to InfoBlox Tag Mapper',
        'mappings_file': MAPPINGS_FILE,
        'mappings_count': len(mapping_manager.mappings)
    })

@app.route('/debug')
def debug():
    """Debug endpoint to check environment"""
    import socket
    return jsonify({
        'working_directory': os.getcwd(),
        'templates_exists': os.path.exists('templates'),
        'index_html_exists': os.path.exists('templates/index.html'),
        'mappings_file': MAPPINGS_FILE,
        'mappings_file_exists': os.path.exists(MAPPINGS_FILE),
        'hostname': socket.gethostname(),
        'port': request.environ.get('SERVER_PORT'),
        'flask_env': os.environ.get('FLASK_ENV', 'not set'),
        'directory_contents': os.listdir('.'),
        'templates_contents': os.listdir('templates') if os.path.exists('templates') else 'templates dir not found'
    })

@app.route('/api/mappings', methods=['GET'])
def get_mappings():
    """Get current mappings"""
    return jsonify({
        'mappings': mapping_manager.mappings,
        'count': len(mapping_manager.mappings)
    })

@app.route('/api/mappings', methods=['POST'])
def update_mapping():
    """Add or update a mapping"""
    data = request.json
    aws_tag = data.get('aws_tag')
    infoblox_ea = data.get('infoblox_ea')
    
    if not aws_tag or not infoblox_ea:
        return jsonify({'error': 'Missing required fields'}), 400
    
    success = mapping_manager.add_mapping(aws_tag, infoblox_ea)
    if success:
        return jsonify({'message': 'Mapping saved successfully'})
    else:
        return jsonify({'error': 'Failed to save mapping'}), 500

@app.route('/api/mappings/<aws_tag>', methods=['DELETE'])
def delete_mapping(aws_tag):
    """Delete a mapping"""
    success = mapping_manager.remove_mapping(aws_tag)
    if success:
        return jsonify({'message': 'Mapping deleted successfully'})
    else:
        return jsonify({'error': 'Mapping not found'}), 404

@app.route('/api/aws-tags', methods=['GET'])
def get_aws_tags():
    """Get available AWS tags from CSV"""
    csv_file = request.args.get('csv_file', 'vpc_data.csv')
    tags = mapping_manager.get_aws_tags_from_csv(csv_file)
    return jsonify({
        'tags': tags,
        'count': len(tags)
    })

@app.route('/api/infoblox-eas', methods=['GET'])
def get_infoblox_eas():
    """Get available InfoBlox Extended Attributes"""
    eas = mapping_manager.get_infoblox_eas()
    # Add suggested EAs that don't exist yet
    existing_eas = set(eas)
    aws_tags = mapping_manager.get_aws_tags_from_csv()
    
    suggested_eas = []
    for tag in aws_tags:
        suggested = mapping_manager.get_suggested_ea_name(tag)
        if suggested not in existing_eas:
            suggested_eas.append(f"{suggested} (suggested)")
    
    all_eas = eas + suggested_eas
    return jsonify({
        'eas': sorted(all_eas),
        'count': len(all_eas)
    })

@app.route('/api/suggest-ea', methods=['POST'])
def suggest_ea():
    """Suggest an EA name for an AWS tag"""
    data = request.json
    aws_tag = data.get('aws_tag', '')
    suggested = mapping_manager.get_suggested_ea_name(aws_tag)
    return jsonify({'suggested': suggested})

@app.route('/api/export-mappings', methods=['GET'])
def export_mappings():
    """Export mappings as JSON"""
    return jsonify(mapping_manager.mappings)

@app.route('/api/import-mappings', methods=['POST'])
def import_mappings():
    """Import mappings from JSON"""
    try:
        data = request.json
        if isinstance(data, dict):
            mapping_manager.save_mappings(data)
            return jsonify({'message': 'Mappings imported successfully'})
        else:
            return jsonify({'error': 'Invalid format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/csv-files', methods=['GET'])
def get_csv_files():
    """Get list of available CSV files"""
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    return jsonify({
        'files': sorted(csv_files),
        'count': len(csv_files)
    })

@app.route('/api/network-views', methods=['POST'])
def get_network_views():
    """Get available network views from InfoBlox"""
    data = request.json
    
    # Use provided credentials or environment defaults
    grid_master = data.get('grid_master') or os.getenv('GRID_MASTER', '192.168.1.222')
    username = data.get('username') or os.getenv('INFOBLOX_USERNAME', 'admin')
    password = data.get('password') or os.getenv('PASSWORD', 'infoblox')
    
    try:
        # Create a client to fetch network views
        client = InfoBloxClient(
            grid_master=grid_master,
            username=username,
            password=password
        )
        
        # Get network views
        response = client._make_request(
            'GET',
            'networkview',
            params={'_return_fields': 'name,comment'}
        )
        
        if response and response.status_code == 200:
            views = [item['name'] for item in response.json()]
            return jsonify({
                'success': True,
                'network_views': views
            })
        else:
            return jsonify({
                'success': False,
                'network_views': ['default'],
                'error': 'Failed to fetch network views'
            })
            
    except Exception as e:
        logger.warning(f"Could not fetch network views: {e}")
        # Return default on error
        return jsonify({
            'success': True,
            'network_views': ['default'],
            'error': str(e)
        })

@app.route('/api/test-connection', methods=['POST'])
def test_connection():
    """Test InfoBlox connection with provided credentials"""
    data = request.json
    
    try:
        # Create a test client with provided credentials
        test_client = InfoBloxClient(
            grid_master=data.get('grid_master'),
            username=data.get('username'),
            password=data.get('password')
        )
        
        # Try to get network views to test the connection
        response = test_client._make_request(
            'GET',
            'networkview',
            params={'_return_fields': 'name,comment'}
        )
        
        if response and response.status_code == 200:
            network_views = [item['name'] for item in response.json()]
            
            # Try to get extended attributes (optional - don't fail if this doesn't work)
            eas = []
            try:
                ea_response = test_client._make_request(
                    'GET',
                    'extensibleattributedef',
                    params={'_return_fields': 'name'}
                )
                if ea_response and ea_response.status_code == 200:
                    eas = [item['name'] for item in ea_response.json()]
            except Exception as e:
                logger.warning(f"Could not fetch extended attributes: {e}")
            
            return jsonify({
                'success': True,
                'network_views': network_views,
                'extended_attributes': eas
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to connect to InfoBlox'
            })
            
    except Exception as e:
        logger.error(f"Connection test failed: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/api/import', methods=['POST'])
def import_networks():
    """Import AWS networks to InfoBlox"""
    data = request.json
    
    # Extract configuration
    config = data.get('config', {})
    aws_data = data.get('aws_data', [])
    tag_mappings = data.get('tag_mappings', {})
    create_missing_eas = data.get('create_missing_eas', False)
    
    # Create a queue for progress updates
    progress_queue = Queue()
    
    def generate():
        """Generate streaming response with progress updates"""
        # Initialize VPC Manager with provided config
        manager = VPCManager(
            grid_master=config.get('grid_master'),
            username=config.get('username'),
            password=config.get('password'),
            network_view=config.get('network_view', 'default')
        )
        
        # Update tag mappings
        manager.tag_mapping = tag_mappings
        
        total_networks = len(aws_data)
        processed = 0
        
        # Send initial status
        yield json.dumps({
            'status': 'Starting import...',
            'progress': 0
        }) + '\n'
        
        # Process each network
        for idx, row in enumerate(aws_data):
            try:
                # Convert row to match expected format
                network_data = {
                    'Name': row.get('Name', ''),
                    'IPv4CIDRBlock': row.get('IPv4CIDRBlock', ''),
                    'VPCId': row.get('VPCId', ''),
                    'Description': row.get('Description', ''),
                    'AccountId': row.get('AccountId', ''),
                    'Region': row.get('Region', ''),
                    'TAGS': row.get('TAGS', '')
                }
                
                # Create network in InfoBlox
                result = manager.create_network_with_eas(
                    network=network_data['IPv4CIDRBlock'],
                    name=network_data['Name'],
                    comment=network_data['Description'],
                    aws_tags=network_data['TAGS'],
                    vpc_id=network_data['VPCId'],
                    account_id=network_data['AccountId'],
                    region=network_data['Region']
                )
                
                processed += 1
                progress = int((processed / total_networks) * 100)
                
                # Send progress update
                yield json.dumps({
                    'progress': progress,
                    'status': f'Processing network {processed}/{total_networks}',
                    'result': {
                        'network': network_data['IPv4CIDRBlock'],
                        'status': 'success' if result else 'error',
                        'message': f'Created network {network_data["Name"]}' if result else 'Failed to create network'
                    }
                }) + '\n'
                
            except Exception as e:
                logger.error(f"Error processing network: {str(e)}")
                processed += 1
                progress = int((processed / total_networks) * 100)
                
                yield json.dumps({
                    'progress': progress,
                    'status': f'Error processing network {processed}/{total_networks}',
                    'result': {
                        'network': row.get('IPv4CIDRBlock', 'Unknown'),
                        'status': 'error',
                        'message': str(e)
                    }
                }) + '\n'
        
        # Send completion status
        yield json.dumps({
            'complete': True,
            'total': processed,
            'progress': 100,
            'status': 'Import completed'
        }) + '\n'
    
    return Response(generate(), mimetype='application/x-ndjson')

def find_free_port(start_port=5000):
    """Find an available port starting from start_port"""
    import socket
    port = start_port
    while port < 65535:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            port += 1
    raise RuntimeError("No free ports available")

if __name__ == '__main__':
    # Create directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    
    # Get port from environment variable or find a free one
    default_port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_ENV', 'production') == 'development'
    
    # Try to use the default port, otherwise find a free one
    try:
        port = default_port
        # Test if port is available
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', port))
    except OSError:
        print(f"\n⚠️  Port {default_port} is already in use, finding a free port...")
        port = find_free_port(default_port + 1)
        print(f"✅ Using port {port} instead")
    
    print("\n🚀 AWS to InfoBlox Tag Mapping Web Interface")
    print("=" * 50)
    print(f"Starting server on http://0.0.0.0:{port}")
    print(f"Mappings file: {MAPPINGS_FILE}")
    print(f"Debug mode: {debug_mode}")
    print("=" * 50)
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)