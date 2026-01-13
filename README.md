# Python Scripts Collection

A comprehensive collection of automation scripts for security, monitoring, system administration, and reporting.

## Overview

This repository contains organized Python utilities for:
- **Log Analysis**: Parse and analyze system logs for security events
- **Monitoring**: Track system usage and automate updates
- **Reconnaissance**: Perform network scanning and service discovery
- **Reporting**: Generate HTML and text reports from collected data
- **Security Scanning**: Check SSL certificates, scan ports, and grab banners
- **System Administration**: Audit environment variables and cleanup temporary files
- **Validation**: Validate manifest files and asset integrity

## Directory Structure

```
python_scripts/
├── log_analysis/           # Log parsing and security event detection
├── monitoring/             # System monitoring and auto-update tools
├── reconnaissance/         # Network reconnaissance and scanning
├── reporting/              # Report generation utilities
├── security_scanning/      # Security testing tools
├── system_administration/  # System cleanup and audit utilities
├── validation/             # Manifest and asset validation
└── README.md              # This file
```

## Quick Start

Each section has its own README with detailed documentation:

- **[Log Analysis](log_analysis/README.md)** - Analyze logs for security threats
- **[Monitoring](monitoring/README.md)** - Monitor system metrics and automate updates
- **[Reconnaissance](reconnaissance/README.md)** - Scan networks and discover services
- **[Reporting](reporting/README.md)** - Generate reports from data
- **[Security Scanning](security_scanning/README.md)** - Test SSL, scan ports, grab banners
- **[System Administration](system_administration/README.md)** - Audit and cleanup system
- **[Validation](validation/README.md)** - Validate manifests and assets

## Requirements

- Python 3.7+
- Standard library modules (most scripts use only built-in modules)
- Optional external dependencies listed in individual tool documentation

## Usage

Each tool can be run individually with:

```bash
python3 script_name.py
```

Refer to individual README files in each section for detailed usage instructions.

## Features

### Log Analysis
- Summarize log files with occurrence counts
- Detect privilege escalation events
- Parse SSH brute force attempts

### Monitoring
- Send email alerts for system events
- Track script execution with timestamps
- Auto-update repositories via git

### Reconnaissance
- Subdomain discovery
- Port scanning
- Service fingerprinting

### Reporting
- HTML report generation
- Log summarization
- Dynamic README generation
- Asset report generation

### Security Scanning
- SSL certificate expiration checking
- Port scanning with customizable ranges
- Service banner grabbing

### System Administration
- Environment variable auditing
- Temporary file cleanup
- OS-specific cleanup configuration
- Sensitive key detection

### Validation
- JSON manifest validation
- Asset existence verification
- Missing asset reporting

## Configuration

Most scripts use environment variables or local configuration files:
- `.env` - Environment variables
- `config.json` - Configuration for cleanup and other tools
- `manifest.json` - Asset manifest for validation

See individual tool documentation for specific configuration requirements.

## Security Considerations

⚠️ **Warning**: Some tools require elevated privileges:
- Log analysis may require access to `/var/log/`
- Cleanup scripts may delete files permanently
- Port scanning should only be used on systems you own or have permission to test

Always review script contents before execution, especially with elevated privileges.

## Contributing

To add new tools:
1. Create a new directory or add to existing section
2. Include proper documentation in tool README
3. Update this main README with new section links
4. Follow existing code style and conventions

## License

See individual tool documentation for specific license information.

## Support

For issues or questions about specific tools, refer to their individual README files.

---

**Last Updated**: January 2026
