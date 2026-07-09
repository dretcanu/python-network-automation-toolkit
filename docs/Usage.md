# Usage Guide

## Overview

This document explains how to use the Python Network Automation Toolkit.

The toolkit is launched through `main.py`.

```bash
python main.py
```

---

## 1. Ping Sweep Scanner

The Ping Sweep Scanner reads subnet information from:

```text
data/subnets.txt
```

Example:

```text
192.168.1.0/24
```

Run from the menu:

```text
1. Ping Sweep Scanner
```

Generated files:

```text
output/ping_results.csv
output/live_hosts.csv
output/scan_summary.txt
```

---

## 2. Device Inventory

The Device Inventory module reads device data from:

```text
data/devices.csv
```

Required CSV headers:

```text
hostname,ip_address,device_type,location,os,role
```

Run from the menu:

```text
2. Device Inventory
```

Generated file:

```text
output/device_inventory_summary.txt
```

---

## 3. Network Health Check

The Network Health Check reads devices from `data/devices.csv` and pings each IP address.

Run from the menu:

```text
3. Network Health Check
```

Generated files:

```text
output/network_health_check.csv
output/network_health_summary.txt
```

---

## 4. Configuration Backup

The Configuration Backup module simulates configuration backup creation for routers and switches listed in `devices.csv`.

Run from the menu:

```text
4. Configuration Backup
```

Generated files:

```text
output/config_backup_summary.txt
output/config_backups/
```

---

## Notes

Some devices may appear as DOWN if they are not reachable from the current computer, are located in a simulated environment, are powered off, or are blocked by firewall rules.
