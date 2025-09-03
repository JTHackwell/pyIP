import ipaddress
import subprocess
import sys

def ip_scanner():
    print("\n--- IP Scanner ---")
    net = input("Enter network address (e.g., 192.168.1.0/24): ").strip()
    try:
        network = ipaddress.ip_network(net, strict=False)
    except ValueError as e:
        print("Invalid network address:", e)
        return

    print(f"Scanning {network.num_addresses} hosts in {network}...\n")
    active_hosts = []
    param = '-n' if sys.platform.startswith('win') else '-c'
    for ip in network.hosts():
        ip_str = str(ip)
        try:
            result = subprocess.run(
                ['ping', param, '1', ip_str],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            if result.returncode == 0:
                print(f"{ip_str} is active")
                active_hosts.append(ip_str)
        except Exception as e:
            print(f"Error pinging {ip_str}: {e}")

    print("\nActive hosts:")
    for host in active_hosts:
        print(host)

if __name__ == "__main__":
    ip_scanner()