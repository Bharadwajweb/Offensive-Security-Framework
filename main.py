from modules.service_enum import service_enum
from modules.recon import recon
from modules.portscan import port_scan
from modules.directory_scan import directory_scan
from modules.web_fingerprint import web_fingerprint
from modules.vulnerability_scan import vulnerability_scan

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

    open_ports = port_scan(
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

    vulnerability_scan(
        open_ports
    )
    service_enum(
        ip,
        open_ports
    )

print("\nScan Completed.")