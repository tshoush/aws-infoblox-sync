# AWS-Sync-Newer

## Multi-Source InfoBlox AWS Network Synchronization Tool

A comprehensive solution for synchronizing AWS network data with InfoBlox in environments containing networks from multiple sources (AWS, Azure, GCP, on-premises).

## Key Features

- **Multi-Source Aware**: Respects networks from AWS, Azure, GCP, and on-premises
- **No Delete Policy**: Only flags AWS-sourced orphaned networks for review
- **Conflict Detection**: Identifies conflicts with networks from any source
- **Hierarchical Management**: Automatically creates containers for larger networks
- **Source Attribution**: All AWS networks tagged with `Source: AWS`
- **Comprehensive Reporting**: HTML reports with downloadable CSV files

## Components

1. **infoblox_aws_comprehensive_analyzer.py** - Analyzes and compares networks
2. **infoblox_aws_network_updater.py** - Applies changes from analysis
3. **infoblox_aws_integration_guide.md** - Complete documentation

## Quick Start

```bash
# 1. Configure environment
cp config.env.example config.env
# Edit config.env with your InfoBlox credentials

# 2. Launch the web interface
python app.py
# This will open http://localhost:8080 in your browser with the presentation hub

# 3. Run analysis (alternatively via command line)
python infoblox_aws_comprehensive_analyzer.py vpc_data.csv --network-view "Production"

# 4. Review generated report
# Open reports/analysis_[timestamp]/analysis_report.html

# 5. Apply changes (after resolving conflicts)
python infoblox_aws_network_updater.py reports/analysis_[timestamp]/analysis_results.json --dry-run
```

## Requirements

- Python 3.7+
- InfoBlox WAPI access
- Required Python packages: pandas, requests, jinja2, python-dotenv

## Installation

```bash
pip install pandas requests jinja2 python-dotenv ipaddress
```

## Documentation

See [infoblox_aws_integration_guide.md](infoblox_aws_integration_guide.md) for detailed documentation.

## License

MIT