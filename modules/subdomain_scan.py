import socket
from datetime import datetime
import os


def subdomain_scan(target):

    print("\n" + "=" * 60)
    print("SUBDOMAIN DISCOVERY MODULE")
    print("=" * 60)

    subdomains = [
        "www",
        "mail",
        "admin",
        "api",
        "dev"
    ]

    found = []

    for sub in subdomains:

        host = f"{sub}.{target}"

        try:
            ip = socket.gethostbyname(host)

            print(f"[FOUND] {host} --> {ip}")

            found.append(
                f"{host} --> {ip}"
            )

        except:
            pass

    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime(
        "outputs/subdomains_%Y%m%d_%H%M%S.txt"
    )

    with open(filename, "w") as f:

        f.write(
            "SUBDOMAIN DISCOVERY REPORT\n"
        )

        f.write("=" * 60 + "\n\n")

        for item in found:
            f.write(item + "\n")

    print(f"\n[+] Report Saved : {filename}")