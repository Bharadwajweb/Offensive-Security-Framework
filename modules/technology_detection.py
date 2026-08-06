import requests
from datetime import datetime
import os

def technology_detection(target):

    print("\n" + "=" * 60)
    print("TECHNOLOGY DETECTION MODULE")
    print("=" * 60)

    technologies = []

    try:
        response = requests.get(
            f"http://{target}",
            timeout=5
        )

        headers = response.headers
        source = response.text.lower()

        server = headers.get("Server", "Unknown")
        powered = headers.get("X-Powered-By", "Unknown")

        print(f"Server : {server}")
        print(f"Powered By : {powered}")

        if "wordpress" in source or "wp-content" in source:
            technologies.append("WordPress")

        if "drupal" in source:
            technologies.append("Drupal")

        if "joomla" in source:
            technologies.append("Joomla")

        if "react" in source:
            technologies.append("React")

        if "angular" in source:
            technologies.append("Angular")

        if "bootstrap" in source:
            technologies.append("Bootstrap")

        if "jquery" in source:
            technologies.append("jQuery")

        for tech in technologies:
            print(f"[+] {tech}")

        os.makedirs("outputs", exist_ok=True)

        filename = datetime.now().strftime(
            "outputs/technology_%Y%m%d_%H%M%S.txt"
        )

        with open(filename, "w", encoding="utf-8") as f:

            f.write("TECHNOLOGY DETECTION REPORT\n")
            f.write("=" * 60 + "\n\n")

            f.write(f"Server : {server}\n")
            f.write(f"Powered By : {powered}\n\n")

            for tech in technologies:
                f.write(f"{tech}\n")

        print(f"\n[+] Report Saved : {filename}")

    except Exception as e:
        print(f"Error : {e}")