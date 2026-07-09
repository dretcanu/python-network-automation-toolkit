import csv
from collections import Counter
from pathlib import Path

from report_utils import report_footer, report_header

from colorama import Fore, Style, init

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
DEVICE_FILE = BASE_DIR / "data" / "devices.csv"
OUTPUT_DIR = BASE_DIR / "output"
SUMMARY_FILE = OUTPUT_DIR / "device_inventory_summary.txt"


def load_devices() -> list[dict[str, str]]:
    if not DEVICE_FILE.exists():
        raise FileNotFoundError(f"Device file not found: {DEVICE_FILE}")

    with DEVICE_FILE.open("r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def print_devices(devices: list[dict[str, str]]) -> None:
    print(f"{Fore.CYAN}Device Inventory")
    print("-" * 95)
    print(f"{'Hostname':<18} {'IP Address':<15} {'Type':<10} {'Location':<15} {'OS':<22} {'Role'}")
    print("-" * 95)

    for device in devices:
        print(
            f"{device['hostname']:<18} "
            f"{device['ip_address']:<15} "
            f"{device['device_type']:<10} "
            f"{device['location']:<15} "
            f"{device['os']:<22} "
            f"{device['role']}"
        )


def write_summary(devices: list[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    type_counts = Counter(device["device_type"] for device in devices)
    location_counts = Counter(device["location"] for device in devices)

    lines = report_header("Device Inventory")
    lines.append(f"Total Devices: {len(devices)}")
    lines.append("")
    lines.append("Devices by Type:")
    for device_type, count in type_counts.items():
        lines.append(f"- {device_type}: {count}")
    lines.append("")
    lines.append("Devices by Location:")
    for location, count in location_counts.items():
        lines.append(f"- {location}: {count}")
    lines.append("")
    lines.append("Inventory:")
    for device in devices:
        lines.append(
            f"- {device['hostname']} | {device['ip_address']} | "
            f"{device['device_type']} | {device['role']}"
        )

    lines.extend(report_footer())

    SUMMARY_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    devices = load_devices()

    print_devices(devices)
    write_summary(devices)

    print()
    print(f"{Fore.GREEN}Inventory loaded successfully.")
    print(f"{Fore.YELLOW}Summary saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()