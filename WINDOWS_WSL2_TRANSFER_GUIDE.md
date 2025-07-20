# Windows WSL2 Transfer Guide

## Files to Copy from Mac to Windows WSL2 Ubuntu

### Essential Files (REQUIRED)

1. **config.env**
   - Contains your InfoBlox credentials and AWS settings
   - Location on Mac: `/Users/tshoush/Preso/Marriot/config.env`
   - IMPORTANT: Contains sensitive credentials - transfer securely

2. **aws_infoblox_vpc_manager_enhanced.py**
   - The main application file with all enhancements
   - Location on Mac: `/Users/tshoush/Preso/Marriot/aws_infoblox_vpc_manager_enhanced.py`

3. **vpc_data.csv** or **vpc_data2.csv**
   - Your AWS VPC data file
   - Location on Mac: `/Users/tshoush/Preso/Marriot/vpc_data*.csv`

### Optional Files

4. **modified_properties_file.csv**
   - Only if you're doing property imports
   - Location on Mac: `/Users/tshoush/Preso/Marriot/modified_properties_file.csv`

5. **Terminal Test Files** (for testing terminal integration)
   - `terminal_integration_summary.md`
   - `terminal_test_results.txt`
   - `terminal_test_detailed.json`
   - `comprehensive_terminal_test.py`
   - `interactive_terminal_test.py`
   - `test_terminal_integration.py`
   - `test_terminal_now.py`
   - `test_terminal_with_error_handling.py`

### Additional Useful Files

6. **Reports and Logs** (if you want historical data)
   - `reports/` directory contents
   - `*.log` files

## Transfer Methods

### Method 1: Direct Copy via Network Share
1. Share the Mac folder over network
2. Access from Windows: `\\<mac-ip>\<share-name>`
3. Copy files to local Windows folder
4. Move to WSL: `\\wsl$\Ubuntu\home\<username>\marriot-infoblox\`

### Method 2: USB Drive
1. Copy files to USB drive from Mac
2. Mount USB in Windows
3. Copy to WSL location

### Method 3: Cloud Storage
1. Upload files to cloud storage (OneDrive, Dropbox, etc.)
2. Download on Windows
3. Move to WSL location

### Method 4: SCP/SFTP (if SSH enabled on Mac)
From WSL Ubuntu:
```bash
scp tshoush@<mac-ip>:/Users/tshoush/Preso/Marriot/config.env ~/marriot-infoblox/
scp tshoush@<mac-ip>:/Users/tshoush/Preso/Marriot/aws_infoblox_vpc_manager_enhanced.py ~/marriot-infoblox/
scp tshoush@<mac-ip>:/Users/tshoush/Preso/Marriot/vpc_data*.csv ~/marriot-infoblox/
```

## WSL2 Setup Steps

1. **Run Setup Script**
   - Use `windows-setup.bat` (Command Prompt)
   - Or `windows-setup.ps1` (PowerShell - recommended)

2. **Copy Files to WSL**
   - Target location: `\\wsl$\Ubuntu\home\<your-username>\marriot-infoblox\`

3. **Complete Setup in WSL**
   ```bash
   wsl -d Ubuntu
   cd ~/marriot-infoblox
   ./setup.sh
   ```

4. **Run Application**
   ```bash
   ./run.sh
   # or manually:
   docker exec -it infoblox-tag-mapper python aws_infoblox_vpc_manager_enhanced.py
   ```

## Important Notes

- The Docker container name is `infoblox-tag-mapper`
- Web interface (if enabled) runs on port 5002
- Logs are stored in `./logs/` directory
- Reports are stored in `./reports/` directory
- Ensure Docker Desktop has WSL2 integration enabled

## Quick Checklist

- [ ] Docker Desktop installed and running
- [ ] WSL2 with Ubuntu installed
- [ ] Docker Desktop WSL integration enabled
- [ ] Files copied to WSL Ubuntu
- [ ] config.env has correct credentials
- [ ] setup.sh executed successfully
- [ ] Container is running (`docker ps`)

## Troubleshooting

If you encounter issues:
1. Check Docker Desktop WSL settings
2. Ensure all files have correct permissions
3. Verify config.env has all required variables
4. Check container logs: `docker logs infoblox-tag-mapper`