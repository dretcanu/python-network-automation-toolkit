import ipaddress
from pathlib import Path

from colorama import Fore, init
from report_utils import report_footer, report_header

init(autoreset=True)

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

SUMMARY_FILE = OUTPUT_DIR / "ip_calculator_summary.txt"


def calculate_subnet(cidr: str) -> dict[str, str]:
    network = ipaddress.ip_network(cidr, strict=False)

    hosts = list(network.hosts())

    first_host = str(hosts[0]) if hosts else "N/A"
    last_host = str(hosts[-1]) if hosts else "N/A"

    return {
        "cidr": str(network),
        "network_address": str(network.network_address),
        "broadcast_address": str(network.broadcast_address),
        "subnet_mask": str(network.netmask),
        "wildcard_mask": str(network.hostmask),
        "prefix_length": f"/{network.prefixlen}",
        "total_addresses": str(network.num_addresses),
        "usable_hosts": str(len(hosts)),
        "first_usable_host": first_host,
        "last_usable_host": last_host,
        "is_private": str(network.is_private),
    }


def write_summary(result: dict[str, str]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    lines = report_header("IP Calculator")

    lines.extend(
        [
            f"CIDR Input: {result['cidr']}",
            "",
            "Subnet Details:",
            f"- Network Address: {result['network_address']}",
            f"- Broadcast Address: {result['broadcast_address']}",
            f"- Subnet Mask: {result['subnet_mask']}",
            f"- Wildcard Mask: {result['wildcard_mask']}",
            f"- Prefix Length: {result['prefix_length']}",
            f"- Total Addresses: {result['total_addresses']}",
            f"- Usable Hosts: {result['usable_hosts']}",
            f"- First Usable Host: {result['first_usable_host']}",
            f"- Last Usable Host: {result['last_usable_host']}",
            f"- Private Network: {result['is_private']}",
        ]
    )

    lines.extend(report_footer())

    SUMMARY_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    print(f"{Fore.CYAN}Python Network Automation Toolkit")
    print(f"{Fore.CYAN}IP Calculator")
    print("-" * 60)

    cidr = input("Enter CIDR subnet, e.g. 192.168.10.0/24: ").strip()

    if not cidr:
        print(f"{Fore.RED}No subnet entered.")
        return

    try:
        result = calculate_subnet(cidr)
    except ValueError:
        print(f"{Fore.RED}Invalid CIDR subnet.")
        return

    print()
    print(f"{Fore.GREEN}Subnet calculation complete.")
    print("-" * 60)
    print(f"CIDR:              {result['cidr']}")
    print(f"Network Address:   {result['network_address']}")
    print(f"Broadcast Address: {result['broadcast_address']}")
    print(f"Subnet Mask:       {result['subnet_mask']}")
    print(f"Wildcard Mask:     {result['wildcard_mask']}")
    print(f"Prefix Length:     {result['prefix_length']}")
    print(f"Total Addresses:   {result['total_addresses']}")
    print(f"Usable Hosts:      {result['usable_hosts']}")
    print(f"First Host:        {result['first_usable_host']}")
    print(f"Last Host:         {result['last_usable_host']}")
    print(f"Private Network:   {result['is_private']}")

    write_summary(result)

    print()
    print(f"{Fore.YELLOW}Summary saved to: {SUMMARY_FILE}")


if __name__ == "__main__":
    main()