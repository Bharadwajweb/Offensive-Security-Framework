import socket
import whois
import dns.resolver
from datetime import datetime
import os


def recon(target):

    print("=" * 60)
    print("RECONNAISSANCE MODULE")
    print("=" * 60)

    try:

        ip = socket.gethostbyname(target)

        os.makedirs("outputs", exist_ok=True)

        filename = datetime.now().strftime(
            "outputs/recon_%Y%m%d_%H%M%S.txt"
        )

        report = open(filename, "w", encoding="utf-8")

        print(f"\n[+] Target : {target}")
        print(f"[+] IP Address : {ip}")

        report.write(f"Target : {target}\n")
        report.write(f"IP Address : {ip}\n\n")

        print("\n[+] WHOIS Information")
        report.write("WHOIS Information\n")

        try:

            w = whois.whois(target)

            print("Registrar :", w.registrar)
            print("Creation Date :", w.creation_date)

            report.write(f"Registrar : {w.registrar}\n")
            report.write(f"Creation Date : {w.creation_date}\n")

        except:

            print("WHOIS Lookup Failed")
            report.write("WHOIS Lookup Failed\n")

        print("\n[+] DNS Records")
        report.write("\nDNS Records\n")

        try:

            ns_records = dns.resolver.resolve(target, "NS")

            for ns in ns_records:

                print("NS :", ns)
                report.write(f"NS : {ns}\n")

        except:

            print("No NS Records Found")
            report.write("No NS Records Found\n")

        print("\n[+] MX Records")
        report.write("\nMX Records\n")

        try:

            mx_records = dns.resolver.resolve(target, "MX")

            for mx in mx_records:

                print("MX :", mx)
                report.write(f"MX : {mx}\n")

        except:

            print("No MX Records Found")
            report.write("No MX Records Found\n")

        report.close()

        print(f"\n[+] Output Saved : {filename}")

        return ip

    except:

        print("Invalid Target")
        return None