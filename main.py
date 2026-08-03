from modules.recon import recon
from modules.portscan import port_scan
from modules.directory_scan import directory_scan
from modules.web_fingerprint import web_fingerprint

print("=" * 60)
print("OFFENSIVE SECURITY AUTOMATION FRAMEWORK")
print("=" * 60)

target = input("Enter Target Domain : ")

ip = recon(target)

if ip:

    start_port = int(
        input("Start Port : ")
    )

    end_port = int(
        input("End Port : ")
    )

    port_scan(
        ip,
        start_port,
        end_port
    )

    directory_scan(
        target
    )

    web_fingerprint(
        target
    )

print("\nScan Completed.")