import csv
import platform
import subprocess
from datetime import datetime
from pathlib import Path

from report_utils import report_footer, report_header

from colorama import Fore, init

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
DEVICE_FILE = BASE_DIR / "data" / "devices.csv"
OUTPUT_DIR = BASE_DIR / "output"

HEALTH_CSV = OUTPUT_DIR / "network_health_check.csv"
HEALTH_SUMMARY = OUTPUT_DIR / "network_health_summary.txt"


def ping_host(ip_address: str) -> str:
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip_address]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip_address]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    return "UP" if result.returncode == 0 else "DOWN"


def load_devices() -> list[dict[str, str]]:
    if not DEVICE_FILE.exists():
        raise FileNotFoundError(f"Device file not found: {DEVICE_FILE}")

    with DEVICE_FILE.open("r", newline="") as file:
        return list(csv.DictReader(file))


def write_csv(results: list[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    with HEALTH_CSV.open("w", newline="") as file:
        fieldnames = [
            "hostname",
            "ip_address",
            "device_type",
            "location",
            "role",
            "status",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def write_summary(results: list[dict[str, str]]) -> None:
    total = len(results)
    up_devices = [device for device in results if device["status"] == "UP"]
    down_devices = [device for device in results if device["status"] == "DOWN"]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "Python Network Automation Toolkit",
        "Network Health Check Summary",
        "",
        f"Scan Time: {timestamp}",
        "",
        "Summary:",
        f"- Total Devices Checked: {total}",
        f"- Devices UP: {len(up_devices)}",
        f"- Devices DOWN: {len(down_devices)}",
        "",
        "Devices UP:",
    ]

    if up_devices:
        for device in up_devices:
            lines.append(
                f"- {device['hostname']} | {device['ip_address']} | "
                f"{device['device_type']} | {device['role']}"
            )
    else:
        lines.append("- None")

    lines.append("")
    lines.append("Devices DOWN:")

    if down_devices:
        for device in down_devices:
            lines.append(
                f"- {device['hostname']} | {device['ip_address']} | "
                f"{device['device_type']} | {device['role']}"
            )
    else:
        lines.append("- None")

    lines.append("")
    lines.append("Note:")
    lines.append(
        "Devices may appear DOWN if they are outside the current local subnet, "
        "powered off, blocked by firewall rules, or only exist inside a simulated lab."
    )

    lines.extend(report_footer())
    
    HEALTH_SUMMARY.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}Network Health Check")
    print("-" * 70)

    devices = load_devices()
    results = []

    for device in devices:
        status = ping_host(device["ip_address"])

        result = {
            "hostname": device["hostname"],
            "ip_address": device["ip_address"],
            "device_type": device["device_type"],
            "location": device["location"],
            "role": device["role"],
            "status": status,
        }

        results.append(result)

        colour = Fore.GREEN if status == "UP" else Fore.RED

        print(
            f"{colour}{device['hostname']:<18} "
            f"{device['ip_address']:<15} "
            f"{device['device_type']:<10} "
            f"{status}"
        )

    write_csv(results)
    write_summary(results)

    print()
    print(f"{Fore.GREEN}Health check complete.")
    print(f"{Fore.YELLOW}CSV saved to: {HEALTH_CSV}")
    print(f"{Fore.YELLOW}Summary saved to: {HEALTH_SUMMARY}")


if __name__ == "__main__":
    main()