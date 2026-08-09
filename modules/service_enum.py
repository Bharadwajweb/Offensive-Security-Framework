from datetime import datetime
import os


def lookup_cves(banner):

    banner = banner.lower()

    cves = []

    if "openssh" in banner:
        cves.append(("CVE-2016-0777", "HIGH"))
        cves.append(("CVE-2015-5600", "MEDIUM"))

    if "apache/2.4.7" in banner:
        cves.append(("CVE-2021-41773", "HIGH"))
        cves.append(("CVE-2021-42013", "CRITICAL"))

    return cves


def detect_os(banner):

    banner = banner.lower()

    if "ubuntu" in banner:
        return "Linux (Ubuntu)"

    if "debian" in banner:
        return "Linux (Debian)"

    if "centos" in banner:
        return "Linux (CentOS)"

    if "windows" in banner:
        return "Windows"

    return "Unknown"


def service_enum(open_ports):

    print("\n" + "=" * 60)
    print("SERVICE ENUMERATION MODULE")
    print("=" * 60)

    findings = []

    for port, service, banner, risk, finding in open_ports:

        print(f"\nPort : {port}")
        print(f"Service : {service}")

        if not banner:
            banner = "Unknown"

        print(f"Banner : {banner}")

        os_name = detect_os(banner)

        print(f"Operating System : {os_name}")

        cves = lookup_cves(banner)

        for cve, severity in cves:
            print(f"[{severity}] {cve}")

        findings.append(
            f"Port: {port}\n"
            f"Service: {service}\n"
            f"Banner: {banner}\n"
            f"Operating System: {os_name}\n"
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