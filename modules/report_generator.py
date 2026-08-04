from datetime import datetime
import os
import json
import csv

def generate_report(target, ip, open_ports):

    print("\n" + "=" * 60)
    print("REPORT GENERATOR MODULE")
    print("=" * 60)

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = f"reports/report_{timestamp}.json"
    csv_file = f"reports/report_{timestamp}.csv"

    report_data = {
        "target": target,
        "ip_address": ip,
        "scan_time": timestamp,
        "open_ports": []
    }

    for port, service, banner, risk, finding in open_ports:

        report_data["open_ports"].append({
            "port": port,
            "service": service,
            "banner": banner,
            "risk": risk,
            "finding": finding
        })

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4)

    with open(csv_file, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Port",
            "Service",
            "Banner",
            "Risk",
            "Finding"
        ])

        for port, service, banner, risk, finding in open_ports:

            writer.writerow([
                port,
                service,
                banner,
                risk,
                finding
            ])

    print(f"[+] JSON Report Saved : {json_file}")
    print(f"[+] CSV Report Saved  : {csv_file}")