import os
import subprocess
import sys
from pathlib import Path

from banner import print_banner

BASE_DIR = Path(__file__).resolve().parent
SCRIPTS_DIR = BASE_DIR / "scripts"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def run_script(script_name):
    script_path = SCRIPTS_DIR / script_name
    subprocess.run([sys.executable, str(script_path)])


while True:
    clear()
    print_banner()
    print()
    print("1. Ping Sweep Scanner")
    print("2. Device Inventory")
    print("3. Network Health Check")
    print("4. Configuration Backup")
    print("5. DNS Lookup")
    print("6. TCP Port Scanner")
    print("7. IP Calculator")
    print("8. Generate Complete Network Report")
    print("9. Exit")
    print()

    choice = input("Select an option: ")

    if choice == "1":
        run_script("ping_sweep.py")
        input("\nPress ENTER to continue...")

    elif choice == "2":
        run_script("device_inventory.py")
        input("\nPress ENTER to continue...")

    elif choice == "3":
        run_script("network_health_check.py")
        input("\nPress ENTER to continue...")

    elif choice == "4":
        run_script("config_backup.py")
        input("\nPress ENTER to continue...")

    elif choice == "5":
        run_script("dns_lookup.py")
        input("\nPress ENTER to continue...")

    elif choice == "6":
        run_script("tcp_port_scanner.py")
        input("\nPress ENTER to continue...")

    elif choice == "7":
        run_script("ip_calculator.py")
        input("\nPress ENTER to continue...")

    elif choice == "8":
        run_script("network_report_generator.py")
        input("\nPress ENTER to continue...")

    elif choice == "9":
        print("Goodbye!")
        break

    else:
        print("\nInvalid option.")
        input("Press ENTER to continue...")