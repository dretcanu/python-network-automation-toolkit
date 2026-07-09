from datetime import datetime
from pathlib import Path

from colorama import Fore, init
from report_utils import report_footer, report_header

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORT_FILE = OUTPUT_DIR / "complete_network_report.txt"

REPORT_SOURCES = [
    ("Ping Sweep Summary", "scan_summary.txt"),
    ("Device Inventory Summary", "device_inventory_summary.txt"),
    ("Network Health Check Summary", "network_health_summary.txt"),
    ("Configuration Backup Summary", "config_backup_summary.txt"),
    ("DNS Lookup Summary", "dns_lookup_summary.txt"),
    ("TCP Port Scan Summary", "port_scan_summary.txt"),
    ("IP Calculator Summary", "ip_calculator_summary.txt"),
]


def read_report_file(filename: str) -> str:
    path = OUTPUT_DIR / filename

    if not path.exists():
        return f"Report file not found: {filename}"

    return path.read_text(encoding="utf-8")


def generate_complete_report() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    lines = report_header("Complete Network Report")

    lines.extend(
        [
            "This report combines the output from all toolkit modules into one consolidated assessment.",
            "",
            f"Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "",
        ]
    )

    for title, filename in REPORT_SOURCES:
        lines.append("-" * 60)
        lines.append(title)
        lines.append("-" * 60)
        lines.append("")
        lines.append(read_report_file(filename))
        lines.append("")

    lines.extend(report_footer())

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}Complete Network Report Generator")
    print("-" * 60)

    generate_complete_report()

    print(f"{Fore.GREEN}Complete network report generated successfully.")
    print(f"{Fore.YELLOW}Report saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()