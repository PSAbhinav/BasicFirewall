import os
import sys
import socket
import ctypes

HOSTS_FILE = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"

# Check for admin rights
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def block_websites(websites):
    try:
        with open(HOSTS_FILE, 'r+') as hosts_file:
            content = hosts_file.read()
            for website in websites:
                for variant in [website, "www." + website]:
                    entry = f"{REDIRECT_IP} {variant}\n"
                    if entry not in content:
                        hosts_file.write(entry)
            print("Websites blocked successfully.")
    except PermissionError:
        print("Permission denied! Run the script as administrator.")
        sys.exit(1)

def unblock_websites(websites):
    try:
        with open(HOSTS_FILE, 'r+') as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)
            for line in lines:
                if not any(site in line for site in websites + ["www." + site for site in websites]):
                    hosts_file.write(line)
            hosts_file.truncate()
        print("Websites unblocked successfully.")
    except PermissionError:
        print("Permission denied! Run the script as administrator.")
        sys.exit(1)

def flush_dns():
    exit_code = os.system("ipconfig /flushdns >nul 2>&1")
    if exit_code == 0:
        print("DNS cache flushed successfully.")
    else:
        print("Error flushing DNS cache.")

def test_website_block(websites):
    for website in websites:
        for test_domain in [website, "www." + website]:
            try:
                ip = socket.gethostbyname(test_domain)
                if ip == REDIRECT_IP:
                    print(f"{test_domain} resolves to {REDIRECT_IP} (BLOCKED by hosts file)")
                else:
                    print(f"{test_domain} resolves to {ip} (NOT BLOCKED)")
            except socket.gaierror:
                print(f"{test_domain} is BLOCKED (cannot resolve)")

if __name__ == "__main__":
    if not is_admin():
        print("Please run this script as Administrator!")
        sys.exit(1)

    print("Simple Firewall Script")
    print("1. Block websites")
    print("2. Unblock websites")
    print("3. Flush DNS cache")
    print("4. Test website block")
    choice = input("Enter your choice: ")

    if choice == "1":
        websites = input("Enter websites to block (comma-separated): ").split(",")
        websites = [site.strip() for site in websites if site.strip()]
        block_websites(websites)
        flush_dns()
    elif choice == "2":
        websites = input("Enter websites to unblock (comma-separated): ").split(",")
        websites = [site.strip() for site in websites if site.strip()]
        unblock_websites(websites)
        flush_dns()
    elif choice == "3":
        flush_dns()
    elif choice == "4":
        websites = input("Enter websites to test (comma-separated): ").split(",")
        websites = [site.strip() for site in websites if site.strip()]
        test_website_block(websites)
    else:
        print("Invalid choice!")

    input("\nPress Enter to exit...")
