from modules.cve_lookup import lookup_cves
from datetime import datetime
import os

def service_enum(ip, open_ports):

    print("\n" + "=" * 60)
    print("SERVICE ENUMERATION MODULE")
    print("=" * 60)

    findings = []

    for port, service, banner, risk, finding in open_ports:

        print(f"\nPort : {port}")
        print(f"Service : {service}")
        print(f"Banner : {banner}")
        cves = lookup_cves(banner)

        for cve, severity in cves:
            print(f"[{severity}] {cve}")

        findings.append(
            f"Port: {port}\nService: {service}\nBanner: {banner}\n"
        )

    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime(
        "outputs/service_enum_%Y%m%d_%H%M%S.txt"
    )

    with open(filename, "w", encoding="utf-8") as f:

        f.write("SERVICE ENUMERATION REPORT\n")
        f.write("=" * 60 + "\n\n")

        for item in findings:
            f.write(item + "\n")

    print(f"\n[+] Report Saved : {filename}")