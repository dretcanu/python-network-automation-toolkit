import csv
import ipaddress
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

from report_utils import report_footer, report_header

from colorama import Fore, Style, init

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
SUBNET_FILE = BASE_DIR / "data" / "subnets.txt"
OUTPUT_DIR = BASE_DIR / "output"

PING_RESULTS_FILE = OUTPUT_DIR / "ping_results.csv"
LIVE_HOSTS_FILE = OUTPUT_DIR / "live_hosts.csv"
SUMMARY_FILE = OUTPUT_DIR / "scan_summary.txt"


def ping_host(ip: str) -> tuple[str, str]:
    system = platform.system().lower()

    if system == "windows":
        command = ["ping", "-n", "1", "-w", "1000", ip]
    else:
        command = ["ping", "-c", "1", "-W", "1", ip]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    status = "UP" if result.returncode == 0 else "DOWN"
    return ip, status


def load_subnets() -> list[str]:
    if not SUBNET_FILE.exists():
        raise FileNotFoundError(f"Subnet file not found: {SUBNET_FILE}")

    subnets = [
        line.strip()
        for line in SUBNET_FILE.read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    if not subnets:
        raise ValueError("No subnets found in data/subnets.txt")

    return subnets


def write_csv(path: Path, headers: list[str], rows: list[tuple[str, str]]) -> None:
    with path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)


def write_summary(
    scanned_subnets: list[str],
    all_results: list[tuple[str, str]],
    live_hosts: list[tuple[str, str]],
) -> None:
    total_hosts = len(all_results)
    live_count = len(live_hosts)
    down_count = total_hosts - live_count

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    summary = f"""Python Network Automation Toolkit
Ping Sweep Scan Summary

Scan Time: {timestamp}

Subnets Scanned:
{chr(10).join(f"- {subnet}" for subnet in scanned_subnets)}

Results:
- Total Hosts Scanned: {total_hosts}
- Live Hosts: {live_count}
- Down Hosts: {down_count}

Live Host List:
{chr(10).join(f"- {ip}" for ip, _ in live_hosts) if live_hosts else "- No live hosts found"}

Output Files:
- ping_results.csv
- live_hosts.csv
- scan_summary.txt
"""

    

    SUMMARY_FILE.write_text(summary, encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}Ping Sweep Scanner")
    print("-" * 45)

    OUTPUT_DIR.mkdir(exist_ok=True)

    subnets = load_subnets()
    all_hosts = []

    for subnet in subnets:
        network = ipaddress.ip_network(subnet, strict=False)
        all_hosts.extend([str(ip) for ip in network.hosts()])

    print(f"Scanning {len(all_hosts)} hosts...\n")

    all_results = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        for ip, status in executor.map(ping_host, all_hosts):
            all_results.append((ip, status))

            if status == "UP":
                print(f"{Fore.GREEN}{ip:<15} {status}")
            else:
                print(f"{Fore.RED}{ip:<15} {status}")

    live_hosts = [(ip, status) for ip, status in all_results if status == "UP"]

    write_csv(PING_RESULTS_FILE, ["ip_address", "status"], all_results)
    write_csv(LIVE_HOSTS_FILE, ["ip_address", "status"], live_hosts)
    write_summary(subnets, all_results, live_hosts)

    print("\n" + "-" * 45)
    print(f"{Fore.GREEN}Live hosts found: {len(live_hosts)}")
    print(f"{Fore.YELLOW}Results saved to:")
    print(f"- {PING_RESULTS_FILE}")
    print(f"- {LIVE_HOSTS_FILE}")
    print(f"- {SUMMARY_FILE}")


if __name__ == "__main__":
    main()