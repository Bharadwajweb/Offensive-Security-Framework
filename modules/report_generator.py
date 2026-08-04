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
    html_file = f"reports/report_{timestamp}.html"

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

    html = f"""
    <html>
    <head>
        <title>Offensive Security Report</title>
        <style>
            body {{
                font-family: Arial;
                background:#f4f4f4;
                margin:20px;
            }}
            h1 {{
                color:#d9534f;
            }}
            table {{
                border-collapse: collapse;
                width:100%;
                background:white;
            }}
            th, td {{
                border:1px solid #ddd;
                padding:8px;
            }}
            th {{
                background:#333;
                color:white;
            }}
        </style>
    </head>
    <body>

    <h1>Offensive Security Framework Report</h1>

    <h3>Target : {target}</h3>
    <h3>IP Address : {ip}</h3>
    <h3>Scan Time : {timestamp}</h3>

    <table>
    <tr>
        <th>Port</th>
        <th>Service</th>
        <th>Banner</th>
        <th>Risk</th>
        <th>Finding</th>
    </tr>
    """

    for port, service, banner, risk, finding in open_ports:

        html += f"""
        <tr>
            <td>{port}</td>
            <td>{service}</td>
            <td>{banner}</td>
            <td>{risk}</td>
            <td>{finding}</td>
        </tr>
        """

    html += """
    </table>
    </body>
    </html>
    """

    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[+] JSON Report Saved : {json_file}")
    print(f"[+] CSV Report Saved  : {csv_file}")
    print(f"[+] HTML Report Saved : {html_file}")