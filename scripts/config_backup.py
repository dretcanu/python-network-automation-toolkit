import csv
from datetime import datetime
from pathlib import Path

from report_utils import report_footer, report_header

from colorama import Fore, init

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
DEVICE_FILE = BASE_DIR / "data" / "devices.csv"
OUTPUT_DIR = BASE_DIR / "output"
BACKUP_DIR = OUTPUT_DIR / "config_backups"
SUMMARY_FILE = OUTPUT_DIR / "config_backup_summary.txt"


def load_devices() -> list[dict[str, str]]:
    if not DEVICE_FILE.exists():
        raise FileNotFoundError(f"Device file not found: {DEVICE_FILE}")

    with DEVICE_FILE.open("r", newline="") as file:
        return list(csv.DictReader(file))


def generate_sample_config(device: dict[str, str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hostname = device["hostname"]
    ip_address = device["ip_address"]
    role = device["role"]
    device_type = device["device_type"]

    return f"""!
! Configuration Backup
! Device: {hostname}
! IP Address: {ip_address}
! Device Type: {device_type}
! Role: {role}
! Backup Time: {timestamp}
!
hostname {hostname}
!
enable secret class
service password-encryption
!
line console 0
 password cisco
 login
!
line vty 0 15
 password cisco
 login
 transport input ssh
!
banner motd #
***********************************************
*  AUTHORISED ACCESS ONLY                    *
*  Simulated backup for portfolio project     *
***********************************************
#
!
end
"""


def backup_configs(devices: list[dict[str, str]]) -> list[dict[str, str]]:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    network_devices = [
        device for device in devices
        if device["device_type"].lower() in ["router", "switch"]
    ]

    for device in network_devices:
        hostname = device["hostname"]
        filename = f"{hostname}_running_config.txt"
        backup_path = BACKUP_DIR / filename

        config_text = generate_sample_config(device)
        backup_path.write_text(config_text, encoding="utf-8")

        results.append(
            {
                "hostname": hostname,
                "ip_address": device["ip_address"],
                "device_type": device["device_type"],
                "role": device["role"],
                "backup_file": str(backup_path),
                "status": "BACKED_UP",
            }
        )

    return results


def write_summary(results: list[dict[str, str]]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "Python Network Automation Toolkit",
        "Configuration Backup Summary",
        "",
        f"Backup Time: {timestamp}",
        "",
        f"Total Network Devices Backed Up: {len(results)}",
        "",
        "Backup Results:",
    ]

    for result in results:
        lines.append(
            f"- {result['hostname']} | {result['ip_address']} | "
            f"{result['device_type']} | {result['status']} | {result['backup_file']}"
        )

    lines.append("")
    lines.append("Note:")
    lines.append(
        "This version simulates configuration backup file generation. "
        "A future version can use SSH/Netmiko to connect to real Cisco devices."
    )

    lines.extend(report_footer())

    SUMMARY_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}Configuration Backup Simulator")
    print("-" * 70)

    devices = load_devices()
    results = backup_configs(devices)
    write_summary(results)

    for result in results:
        print(
            f"{Fore.GREEN}{result['hostname']:<18} "
            f"{result['ip_address']:<15} "
            f"{result['device_type']:<10} "
            f"{result['status']}"
        )

    print()
    print(f"{Fore.GREEN}Configuration backup complete.")
    print(f"{Fore.YELLOW}Backups saved to: {BACKUP_DIR}")
    print(f"{Fore.YELLOW}Summary saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()