from datetime import datetime
import os

def create_dashboard(target, ip, open_ports=None):

    os.makedirs("dashboard", exist_ok=True)

    filename = datetime.now().strftime(
        "dashboard/dashboard_%Y%m%d_%H%M%S.html"
    )

    rows = ""

    if open_ports:

        for port, service, banner, risk, finding in open_ports:

            rows += f"""
            <tr>
                <td>{port}</td>
                <td>{service}</td>
                <td>{risk}</td>
                <td>{finding}</td>
            </tr>
            """

    html = f"""
    <html>
    <head>
        <title>Security Dashboard</title>

        <style>

        body {{
            font-family: Arial;
            background: #f4f4f4;
            margin: 20px;
        }}

        h1 {{
            color: #d9534f;
        }}

        .card {{
            background: white;
            padding: 15px;
            margin-bottom: 15px;
            border-radius: 8px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
        }}

        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
        }}

        th {{
            background: #333;
            color: white;
        }}

        </style>

    </head>

    <body>

        <h1>Offensive Security Dashboard</h1>

        <div class="card">
            <h2>Target Information</h2>
            <p><b>Target:</b> {target}</p>
            <p><b>IP Address:</b> {ip}</p>
        </div>

        <div class="card">
            <h2>Open Ports</h2>

            <table>

                <tr>
                    <th>Port</th>
                    <th>Service</th>
                    <th>Risk</th>
                    <th>Finding</th>
                </tr>

                {rows}

            </table>

        </div>

    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[+] Dashboard Saved : {filename}")