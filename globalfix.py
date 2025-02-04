import os
import subprocess
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def set_dns(dns_server="8.8.8.8"):
    """
    Set DNS server for all network interfaces to the specified DNS server.
    Default is Google's public DNS server: 8.8.8.8
    """
    try:
        subprocess.check_call(
            ['netsh', 'interface', 'ip', 'set', 'dns', 'name="Ethernet"', 'source=static', f'addr={dns_server}', 'register=PRIMARY']
        )
        subprocess.check_call(
            ['netsh', 'interface', 'ip', 'set', 'dns', 'name="Wi-Fi"', 'source=static', f'addr={dns_server}', 'register=PRIMARY']
        )
        print(f"DNS server set to {dns_server} successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set DNS server. Error: {e}")

def reset_network_settings():
    """
    Reset network settings to fix connectivity issues.
    """
    try:
        subprocess.check_call(['netsh', 'winsock', 'reset'])
        subprocess.check_call(['netsh', 'int', 'ip', 'reset'])
        print("Network settings reset successfully. Please restart your computer.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reset network settings. Error: {e}")

def optimize_connection():
    """
    Optimize network settings for better connectivity.
    """
    try:
        subprocess.check_call(['netsh', 'interface', 'tcp', 'set', 'global', 'autotuninglevel=normal'])
        subprocess.check_call(['netsh', 'interface', 'tcp', 'set', 'heuristics', 'disabled'])
        print("Network connection optimized successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to optimize network connection. Error: {e}")

def main():
    if not is_admin():
        print("This script requires administrative privileges. Please run it as an administrator.")
        return
    
    print("Welcome to GlobalFix - Network Optimization Tool")
    print("Select an option:")
    print("1. Set DNS Server")
    print("2. Reset Network Settings")
    print("3. Optimize Connection")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        dns_server = input("Enter DNS server address (default is 8.8.8.8): ") or "8.8.8.8"
        set_dns(dns_server)
    elif choice == '2':
        reset_network_settings()
    elif choice == '3':
        optimize_connection()
    elif choice == '4':
        print("Exiting GlobalFix. Goodbye!")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()