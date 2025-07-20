# AWS to InfoBlox Tag Mapping Web Interface

This web interface allows you to manage the mapping between AWS tags and InfoBlox Extended Attributes dynamically.

## Features

- **Visual Mapping Management**: Easy-to-use interface for creating, editing, and deleting tag mappings
- **Dropdown Menus**: Select from available AWS tags (extracted from your CSV file) and InfoBlox Extended Attributes
- **Auto-Mapping**: Automatically create mappings for unmapped tags with suggested EA names
- **Import/Export**: Save and load mapping configurations
- **Real-time Updates**: See which AWS tags are unmapped and need attention
- **Bulk Operations**: Auto-map all unmapped tags or reset to defaults

## Installation

1. Install required dependencies:
```bash
pip install -r requirements_web.txt
```

2. Ensure your `config.env` file is properly configured with InfoBlox credentials

## Usage

### Starting the Web Interface

Run the web application:
```bash
python tag_mapping_web_app.py
```

The interface will be available at: http://localhost:5000

### Using the Interface

1. **View Current Mappings**: The main tab shows all configured tag mappings
2. **Add New Mapping**: Click "Add Mapping" to create a new mapping
3. **Edit Mapping**: Click the edit icon next to any mapping to modify it
4. **Delete Mapping**: Click the trash icon to remove a mapping
5. **View Unmapped Tags**: Switch to the "Unmapped AWS Tags" tab to see tags that need mapping
6. **Auto-Map Tags**: Use the bulk operations tab to automatically map all unmapped tags

### Integration with Main Script

Use the enhanced version of the script that reads from the tag mappings file:

```bash
# Uses mappings from tag_mappings.json
python aws_infoblox_vpc_manager_with_web.py

# Or continue using the original script (with hardcoded mappings)
python aws_infoblox_vpc_manager_complete.py
```

## How It Works

1. The web interface creates/updates a `tag_mappings.json` file
2. The enhanced script (`aws_infoblox_vpc_manager_with_web.py`) reads this file
3. If no custom mappings exist, default mappings are used
4. All AWS tags are mapped to InfoBlox Extended Attributes based on the configuration

## Tag Mapping Examples

| AWS Tag | InfoBlox EA |
|---------|-------------|
| Name | aws_name |
| Environment | environment |
| Owner | owner |
| Project | project |
| AccountId | aws_account_id |
| Region | aws_region |
| VpcId | aws_vpc_id |

## Files Created

- `tag_mappings.json`: Stores the custom tag mappings
- `templates/index.html`: Web interface HTML template
- `tag_mapping_web_app.py`: Flask web application

## Notes

- The interface will attempt to connect to InfoBlox to fetch available Extended Attributes
- If InfoBlox is not accessible, you can still manage mappings manually
- Suggested EA names follow the pattern: `aws_<tag_name_lowercase>`
- All spaces and hyphens in tag names are converted to underscores in EA names