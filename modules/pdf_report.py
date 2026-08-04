from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
import os


def generate_pdf_report(target, open_ports, vulnerabilities):

    os.makedirs("reports", exist_ok=True)

    filename = datetime.now().strftime(
        "reports/report_%Y%m%d_%H%M%S.pdf"
    )

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "OFFENSIVE SECURITY REPORT",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"<b>Target:</b> {target}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Open Ports</b>",
            styles["Heading2"]
        )
    )

    for port, service, banner, risk, finding in open_ports:

        content.append(
            Paragraph(
                f"Port: {port} | Service: {service} | Risk: {risk}",
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>Vulnerabilities</b>",
            styles["Heading2"]
        )
    )

    for item in vulnerabilities:

        content.append(
            Paragraph(
                item,
                styles["Normal"]
            )
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            "<b>CVE Findings</b>",
            styles["Heading2"]
        )
    )

    for port, service, banner, risk, finding in open_ports:

        content.append(
            Paragraph(
                f"{finding} ({risk})",
                styles["Normal"]
            )
        )

    doc.build(content)

    print(
        f"[+] PDF Report Saved : {filename}"
    )