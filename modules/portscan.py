import socket
import threading
from datetime import datetime
import os

from modules.vulnerability_scan import classify_risk

open_ports = []
lock = threading.Lock()


def grab_banner(ip, port):

    try:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        s.connect((ip, port))

        if port == 80:
            s.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")

        banner = s.recv(1024)

        s.close()

        return banner.decode(errors="ignore").strip()

    except:

        return "Unknown"


def scan_port(target_ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((target_ip, port))

    if result == 0:

        try:
            service = socket.getservbyport(port)

        except:
            service = "Unknown"

        banner = grab_banner(target_ip, port)

        risk, finding = classify_risk(
            port,
            banner
        )

        with lock:

            open_ports.append(
                (
                    port,
                    service,
                    banner,
                    risk,
                    finding
                )
            )

            print(
                f"[OPEN] {port} | {service} | {risk}"
            )

    sock.close()


def port_scan(target_ip, start_port, end_port):

    print("\n" + "=" * 60)
    print("PORT SCANNING MODULE")
    print("=" * 60)

    open_ports.clear()

    threads = []

    for port in range(start_port, end_port + 1):

        t = threading.Thread(
            target=scan_port,
            args=(target_ip, port)
        )

        threads.append(t)

        t.start()

    for t in threads:
        t.join()

    os.makedirs("outputs", exist_ok=True)

    filename = datetime.now().strftime(
        "outputs/portscan_%Y%m%d_%H%M%S.txt"
    )

    with open(filename, "w", encoding="utf-8") as report:

        report.write("=" * 80 + "\n")
        report.write("PORT SCAN REPORT\n")
        report.write("=" * 80 + "\n\n")

        report.write(
            "PORT | SERVICE | RISK | FINDING\n"
        )

        report.write(
            "-" * 80 + "\n"
        )

        for port, service, banner, risk, finding in sorted(open_ports):

            report.write(
                f"{port} | {service} | {risk} | {finding}\n"
            )

    print(
        f"\n[+] Report Saved : {filename}"
    )

    return open_ports