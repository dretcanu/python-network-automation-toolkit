import socket
from datetime import datetime
from pathlib import Path

from report_utils import report_footer, report_header

from colorama import Fore, init

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
SUMMARY_FILE = OUTPUT_DIR / "dns_lookup_summary.txt"


def forward_lookup(hostname: str) -> list[str]:
    try:
        _, _, ip_addresses = socket.gethostbyname_ex(hostname)
        return ip_addresses
    except socket.gaierror:
        return []


def reverse_lookup(ip_address: str) -> str | None:
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return None


def write_summary(query: str, lookup_type: str, results: list[str] | str | None) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    lines = [
        "Python Network Automation Toolkit",
        "DNS Lookup Summary",
        "",
        f"Lookup Time: {timestamp}",
        f"Lookup Type: {lookup_type}",
        f"Query: {query}",
        "",
        "Results:",
    ]

    if isinstance(results, list):
        if results:
            for result in results:
                lines.append(f"- {result}")
        else:
            lines.append("- No DNS records found")
    elif isinstance(results, str):
        lines.append(f"- {results}")
    else:
        lines.append("- No reverse DNS record found")

    lines.extend(report_footer())
    
    SUMMARY_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}DNS Lookup Tool")
    print("-" * 50)
    print("1. Forward lookup hostname to IP")
    print("2. Reverse lookup IP to hostname")
    print()

    choice = input("Select an option: ").strip()

    if choice == "1":
        hostname = input("Enter hostname, e.g. google.com: ").strip()
        results = forward_lookup(hostname)

        print()
        if results:
            print(f"{Fore.GREEN}IP addresses found:")
            for ip in results:
                print(f"- {ip}")
        else:
            print(f"{Fore.RED}No DNS records found.")

        write_summary(hostname, "Forward Lookup", results)

    elif choice == "2":
        ip_address = input("Enter IP address, e.g. 8.8.8.8: ").strip()
        result = reverse_lookup(ip_address)

        print()
        if result:
            print(f"{Fore.GREEN}Hostname found:")
            print(f"- {result}")
        else:
            print(f"{Fore.RED}No reverse DNS record found.")

        write_summary(ip_address, "Reverse Lookup", result)

    else:
        print(f"{Fore.RED}Invalid option.")
        return

    print()
    print(f"{Fore.YELLOW}Summary saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()