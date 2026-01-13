# Project Structure - Enterprise Standard Layout

## Overview
This repository has been reorganized into a logical, enterprise-standard file system structure for better maintainability, scalability, and clarity.

## Directory Structure

```
python_scripts/
├── src/                              # Source code organized by function
│   ├── security_scanning/            # SSL checks, port scanning, service fingerprinting
│   │   ├── check_ssl.py
│   │   ├── netcat_banner.py
│   │   └── Port_Scan.py
│   │
│   ├── log_analysis/                 # Log forensics and threat analysis
│   │   ├── log_summary_report.py
│   │   ├── priv_escalation_detector.py
│   │   └── ssh_brute_parser.py
│   │
│   ├── system_administration/        # System maintenance and environment management
│   │   ├── audit_env.py
│   │   ├── cleanup.py
│   │   ├── Cleanup_Temp.py
│   │   ├── Env_Audit.py
│   │   └── scan_env_file.py
│   │
│   ├── reporting/                    # Report generation and documentation tools
│   │   ├── HTML_Report.py
│   │   ├── Log_Summarizer.py
│   │   ├── README_Generator.py
│   │   └── report_generator.py
│   │
│   ├── monitoring/                   # Notifications and tracking systems
│   │   ├── Email_Notifier.py
│   │   ├── Self_Updater.py
│   │   └── Usage_Tracker.py
│   │
│   ├── reconnaissance/               # Automated recon and scanning modules
│   │   ├── auto_rec_main.py
│   │   └── modules/
│   │       ├── port_scan.py
│   │       ├── service_fingerPrint.py
│   │       └── subdomain_scan.py
│   │
│   └── validation/                   # Data and manifest validation tools
│       ├── Manifest_Validator.py
│       └── validate_manifest.py
│
├── config/                           # Configuration files
│   ├── cleanup_config.json
│   └── manifest.json
│
├── docs/                             # Documentation and README files
│   └── README.md
│
├── licenses/                         # License files from all modules
│   ├── License_Cleanup_CLI.txt
│   ├── License_Log_Forensics_Toolkit.txt
│   ├── License_Manifest_Validator_CLI.txt
│   ├── License_Recon_Automation_CLI.txt
│   └── License_Secure_Env_Audit.txt
│
└── STRUCTURE.md                      # This file
```

## Module Categories

### `src/security_scanning/`
**Purpose**: Network and service security analysis
- SSL/TLS certificate validation
- Port scanning and discovery
- Service fingerprinting and banner grabbing

### `src/log_analysis/`
**Purpose**: Security incident investigation and log forensics
- Log parsing and analysis
- Privilege escalation detection
- SSH brute force attack analysis

### `src/system_administration/`
**Purpose**: System maintenance and environment management
- Temporary file cleanup
- Environment variable auditing
- System configuration scanning

### `src/reporting/`
**Purpose**: Report generation and data presentation
- HTML report generation
- Log summarization
- Documentation auto-generation
- Custom report formatting

### `src/monitoring/`
**Purpose**: Continuous monitoring and notifications
- Email alert notifications
- Usage and activity tracking
- Automated system updates

### `src/reconnaissance/`
**Purpose**: Automated network reconnaissance with modular approach
- Main reconnaissance orchestration
- Port scanning modules
- Service identification modules
- Subdomain enumeration modules

### `src/validation/`
**Purpose**: Data integrity and configuration validation
- Manifest file validation
- Configuration verification
- Data format checking

### `config/`
**Purpose**: Centralized configuration management
- Application settings
- Module configurations
- Manifest definitions

### `docs/`
**Purpose**: All documentation
- Project README files
- Module documentation
- Usage guides

### `licenses/`
**Purpose**: License compliance and attribution
- Individual module licenses
- Legal compliance files

## Benefits of This Structure

✓ **Clear Separation of Concerns**: Each module category has a distinct purpose
✓ **Scalability**: Easy to add new modules within existing categories
✓ **Maintainability**: Logical grouping makes code easier to locate and manage
✓ **Enterprise Standards**: Follows industry best practices for project organization
✓ **Configuration Management**: Centralized config folder for consistency
✓ **Documentation**: Separate docs folder for easy access to guides
✓ **Compliance**: Dedicated licenses folder for legal requirements
✓ **Modularity**: Clear module structure encourages code reuse

## Migration Notes

- All files have been reorganized from their original locations
- File functionality remains unchanged
- Original folder names (Cross_Com_Py, Log_Forensics_Toolkit, etc.) have been removed
- Duplicated functionality has been consolidated where appropriate
- All configuration and license files are now centrally accessible
