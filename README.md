<div align="center">



\# 🐍 Python Network Automation Toolkit



\### Professional Python toolkit for automating common Network Engineering and Infrastructure tasks



\[!\[Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge\&logo=python)](https://www.python.org/)

\[!\[Automation](https://img.shields.io/badge/Network-Automation-success?style=for-the-badge)]()

\[!\[CLI](https://img.shields.io/badge/CLI-Application-orange?style=for-the-badge)]()

\[!\[License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)]()



\---



\*A portfolio project demonstrating practical Python scripting, network automation, infrastructure management and technical documentation.\*



</div>



\---



\## 📖 Table of Contents



\- \[Project Overview](#-project-overview)

\- \[Features](#-features)

\- \[Toolkit Architecture](#-toolkit-architecture)

\- \[Installation](#-installation)

\- \[Quick Start](#-quick-start)

\- \[Modules](#-modules)

\- \[Repository Structure](#-repository-structure)

\- \[Technologies Used](#-technologies-used)

\- \[Skills Demonstrated](#-skills-demonstrated)

\- \[Future Improvements](#-future-improvements)

\- \[Author](#-author)



\---



\# 📖 Project Overview



The \*\*Python Network Automation Toolkit\*\* is a modular command-line application developed to automate common networking and infrastructure tasks.



The project demonstrates practical Python skills used by Network Engineers, Infrastructure Engineers and IT Support professionals.



Rather than being a single script, the toolkit combines multiple automation utilities into one application with a menu-driven interface.



The current version includes:



\- Network discovery

\- Device inventory management

\- Network health monitoring

\- Configuration backup simulation

\- DNS lookups

\- TCP port scanning

\- IP subnet calculations



The project has been developed as part of my professional networking portfolio and follows standard Python project organisation, including virtual environments, modular code, documentation and GitHub best practices.



\---



\# 🚀 Features



The toolkit currently includes \*\*seven fully functional automation modules\*\* designed to demonstrate practical network engineering and infrastructure administration skills.



| Module | Description | Output |

|---------|-------------|--------|

| ✅ Ping Sweep Scanner | Scans an IPv4 subnet and identifies reachable hosts using multithreaded ICMP requests. | CSV + TXT Report |

| ✅ Device Inventory | Reads and summarises network devices from a CSV inventory database. | TXT Report |

| ✅ Network Health Check | Verifies device availability by pinging every device in the inventory. | CSV + TXT Report |

| ✅ Configuration Backup | Simulates automated configuration backups for routers and switches. | Backup Files + TXT Report |

| ✅ DNS Lookup | Performs forward and reverse DNS lookups using Python's socket library. | TXT Report |

| ✅ TCP Port Scanner | Scans common TCP ports and reports open/closed services. | CSV + TXT Report |

| ✅ IP Calculator | Calculates complete IPv4 subnet information from CIDR notation. | TXT Report |



\---



\# 🏗 Toolkit Architecture



The toolkit is designed around a simple modular architecture. Each module performs a single task while `main.py` provides a central menu-driven interface.



```text

&#x20;                        main.py

&#x20;                           │

&#x20;    ┌──────────┬───────────┼───────────┬──────────┐

&#x20;    │          │           │           │          │

&#x20;Ping Sweep  Inventory   Health     Config      DNS

&#x20;  Scanner               Check      Backup     Lookup

&#x20;    │          │           │           │          │

&#x20;    └──────────┴───────────┼───────────┴──────────┘

&#x20;                           │

&#x20;                   TCP Port Scanner

&#x20;                           │

&#x20;                    IP Calculator

```



Every module is independent and can be executed either from the main application or individually for testing and development.



\---



\# 🛠 Modules



\## 1️⃣ Ping Sweep Scanner



\*\*Purpose\*\*



Discovers live hosts within one or more IPv4 subnets.



\### Demonstrated Skills



\- Python threading

\- IP address handling

\- ICMP testing

\- CSV generation

\- Report generation



\### Generated Files



```text

output/

├── ping\_results.csv

├── live\_hosts.csv

└── scan\_summary.txt

```



\---



\## 2️⃣ Device Inventory



Maintains a structured inventory of network devices using CSV.



\### Demonstrated Skills



\- CSV parsing

\- Data validation

\- Inventory reporting



\### Generated Files



```text

output/

└── device\_inventory\_summary.txt

```



\---



\## 3️⃣ Network Health Check



Performs availability testing against every device listed in the inventory.



\### Demonstrated Skills



\- Automated monitoring

\- Network diagnostics

\- Status reporting



\### Generated Files



```text

output/

├── network\_health\_check.csv

└── network\_health\_summary.txt

```



\---



\## 4️⃣ Configuration Backup



Creates simulated configuration backup files for routers and switches.



Although the current version generates sample configurations, the design allows future integration with SSH automation tools such as \*\*Netmiko\*\* or \*\*Paramiko\*\*.



\### Generated Files



```text

output/

├── config\_backup\_summary.txt

└── config\_backups/

```



\---



\## 5️⃣ DNS Lookup



Performs:



\- Forward DNS Lookup

\- Reverse DNS Lookup



using Python's built-in `socket` module.



\### Generated Files



```text

output/

└── dns\_lookup\_summary.txt

```



\---



\## 6️⃣ TCP Port Scanner



Scans a predefined set of commonly used TCP ports.



Example services:



\- SSH

\- HTTP

\- HTTPS

\- SMTP

\- FTP

\- DNS

\- RDP



\### Generated Files



```text

output/

├── port\_scan\_results.csv

└── port\_scan\_summary.txt

```



\---



\## 7️⃣ IP Calculator



Calculates complete subnet information from CIDR notation.



Example output:



\- Network Address

\- Broadcast Address

\- Subnet Mask

\- Wildcard Mask

\- First Host

\- Last Host

\- Total Addresses

\- Usable Hosts



\### Generated Files



```text

output/

└── ip\_calculator\_summary.txt

```



\# ⚙️ Installation



\## Clone the Repository



```bash

git clone https://github.com/dretcanu/python-network-automation-toolkit.git

cd python-network-automation-toolkit

```



\---



\## Create a Virtual Environment



Windows (PowerShell)



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

```



Linux / macOS



```bash

python3 -m venv .venv

source .venv/bin/activate

```



\---



\## Install Dependencies



```bash

pip install -r requirements.txt

```



\---



\# ▶️ Quick Start



Launch the toolkit:



```bash

python main.py

```



The main menu will appear:



```text

=======================================================

&#x20;Python Network Automation Toolkit v2.0

=======================================================



1\. Ping Sweep Scanner

2\. Device Inventory

3\. Network Health Check

4\. Configuration Backup

5\. DNS Lookup

6\. TCP Port Scanner

7\. IP Calculator

8\. Exit

```



Select the desired module and follow the on-screen prompts.



\---



\# 📁 Repository Structure



```text

python-network-automation-toolkit/



├── main.py

├── README.md

├── LICENSE

├── requirements.txt

├── .gitignore

│

├── scripts/

│   ├── report\_utils.py

│   ├── ping\_sweep.py

│   ├── device\_inventory.py

│   ├── network\_health\_check.py

│   ├── config\_backup.py

│   ├── dns\_lookup.py

│   ├── tcp\_port\_scanner.py

│   └── ip\_calculator.py

│

├── data/

│   ├── devices.csv

│   └── subnets.txt

│

├── output/

│

├── docs/

│   ├── Installation.md

│   ├── Usage.md

│   ├── Testing.md

│   ├── Architecture.md

│   └── Lessons-Learned.md

│

└── screenshots/

```



\---



\# 🧰 Technologies Used



\### Programming



\- Python 3.13

\- Virtual Environments (venv)



\### Python Modules



\- socket

\- ipaddress

\- csv

\- pathlib

\- subprocess

\- concurrent.futures

\- datetime

\- colorama



\### Networking Concepts



\- IPv4 Addressing

\- CIDR

\- ICMP

\- DNS

\- TCP

\- Network Discovery

\- Port Scanning

\- Configuration Management

\- Device Inventory

\- Health Monitoring



\---



\# 💡 Skills Demonstrated



This project demonstrates practical experience with:



\## Python



\- Modular application development

\- File handling

\- Exception handling

\- CLI applications

\- CSV processing

\- Report generation



\## Networking



\- IPv4 subnetting

\- Network discovery

\- Device inventory

\- DNS resolution

\- TCP connectivity

\- Port scanning

\- Configuration management



\## Professional Practices



\- GitHub repository structure

\- Technical documentation

\- Virtual environments

\- Modular software design

\- Clean project organisation



\---



\# 🗺️ Roadmap



Future improvements planned for the toolkit include:



\- SSH automation using Netmiko

\- Multi-threaded port scanning

\- HTML dashboard

\- SQLite device inventory

\- REST API integration

\- SNMP monitoring

\- Scheduled health checks

\- Logging framework

\- YAML inventory support

\- Configuration comparison

\- Email alerts

\- Automated report generation



\---



\# 📊 Project Statistics



| Metric | Value |

|---------|------:|

| Python Modules | 7 |

| CLI Application | 1 |

| Generated Report Types | 8+ |

| CSV Outputs | Multiple |

| TXT Reports | Multiple |

| Supported Operating Systems | Windows / Linux / macOS |

| Architecture | Modular |



\---



\# 👨‍💻 About the Author



\## Vasile C. Dretcanu



Aspiring \*\*Network Engineer\*\*, \*\*Infrastructure Engineer\*\* and \*\*Systems Administrator\*\*, currently building a practical portfolio focused on networking, infrastructure automation and enterprise technologies.



\### Areas of Interest



\- Enterprise Networking

\- Infrastructure Engineering

\- Python Automation

\- Windows Server

\- Cisco Technologies

\- Network Security



GitHub:



\*\*https://github.com/dretcanu\*\*



\---



\# 📄 License



This project is licensed under the MIT License.



\---



<div align="center">



\### ⭐ If you found this project interesting, please consider starring the repository.



Thank you for visiting!



</div>

