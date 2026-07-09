# 🐍 Network Automation Toolkit

> **Built with Python**\
> A professional command-line toolkit for automating common Network
> Engineering and Infrastructure tasks.

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Automation](https://img.shields.io/badge/Automation-Network-success?style=for-the-badge)
![CLI](https://img.shields.io/badge/Application-CLI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

------------------------------------------------------------------------

## 📸 Application Preview

![Main Menu](screenshots/01-main-menu.png)

## 🚀 Project Highlights

-   ✅ 8 integrated networking modules
-   ✅ Menu-driven CLI application
-   ✅ Modular Python architecture
-   ✅ Automated report generation
-   ✅ CSV and TXT exports
-   ✅ Cross-platform support

------------------------------------------------------------------------

## ✨ Features

  Module                    Description
  ------------------------- ------------------------------------
  Ping Sweep Scanner        Discover live hosts on a subnet
  Device Inventory          Manage a CSV inventory of devices
  Network Health Check      Verify device availability
  Configuration Backup      Simulate router and switch backups
  DNS Lookup                Forward and reverse DNS queries
  TCP Port Scanner          Scan common TCP ports
  IP Calculator             Calculate IPv4 subnet information
  Complete Network Report   Combine all reports into one

------------------------------------------------------------------------

## 📷 Screenshots

### Main Menu

![Main Menu](screenshots/01-main-menu.png)

### Core Modules

  -------------------------------------------------------------------------------
  Ping Sweep                           Device Inventory
  ------------------------------------ ------------------------------------------
  ![](screenshots/02-ping-sweep.png)   ![](screenshots/03-device-inventory.png)

  -------------------------------------------------------------------------------

  ------------------------------------------------------------------------------------------
  Health Check                                   Configuration Backup
  ---------------------------------------------- -------------------------------------------
  ![](screenshots/04-network-health-check.png)   ![](screenshots/05-config-backup.png)

  ------------------------------------------------------------------------------------------

  -------------------------------------------------------------------------------
  DNS Lookup                           TCP Port Scanner
  ------------------------------------ ------------------------------------------
  ![](screenshots/06-dns-lookup.png)   ![](screenshots/07-port-scanner.png)

  -------------------------------------------------------------------------------

### IP Calculator

![](screenshots/08-ip-calculator.png)

### Complete Network Report

![](screenshots/09-complete-report.png)

------------------------------------------------------------------------

## 🏗 Architecture

``` text
main.py
 ├── Ping Sweep Scanner
 ├── Device Inventory
 ├── Network Health Check
 ├── Configuration Backup
 ├── DNS Lookup
 ├── TCP Port Scanner
 ├── IP Calculator
 └── Complete Network Report
```

------------------------------------------------------------------------

## ⚡ Quick Start

``` bash
git clone https://github.com/dretcanu/python-network-automation-toolkit.git
cd python-network-automation-toolkit
python -m venv .venv
pip install -r requirements.txt
python main.py
```

------------------------------------------------------------------------

## 📁 Repository Structure

``` text
python-network-automation-toolkit/
├── main.py
├── banner.py
├── README.md
├── requirements.txt
├── scripts/
├── data/
├── docs/
├── output/
└── screenshots/
```

------------------------------------------------------------------------

## 🛠 Technologies

-   Python 3.13
-   socket
-   ipaddress
-   pathlib
-   csv
-   subprocess
-   concurrent.futures
-   colorama

------------------------------------------------------------------------

## 💼 Skills Demonstrated

**Networking**

-   IPv4 Addressing
-   CIDR Subnetting
-   DNS
-   TCP/IP
-   Port Scanning
-   Network Monitoring

**Python**

-   Modular programming
-   CLI development
-   CSV processing
-   File handling
-   Report generation
-   Exception handling

------------------------------------------------------------------------

## 🚀 Future Roadmap

-   SSH automation with Netmiko
-   SNMP monitoring
-   REST API integration
-   HTML reports
-   SQLite inventory
-   Logging improvements

------------------------------------------------------------------------

## 👨‍💻 About the Author

**Vasile C. Dretcanu**

Aspiring Network & Infrastructure Engineer building practical networking
and automation projects.

GitHub: https://github.com/dretcanu

------------------------------------------------------------------------

## 📄 License

Released under the MIT License.
