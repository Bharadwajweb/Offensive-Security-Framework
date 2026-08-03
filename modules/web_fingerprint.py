import requests

def web_fingerprint(target):

    print("\n" + "=" * 60)
    print("WEB FINGERPRINTING MODULE")
    print("=" * 60)

    try:

        url = f"http://{target}"

        response = requests.get(
            url,
            timeout=5
        )

        print(
            f"Server : {response.headers.get('Server','Unknown')}"
        )

        print(
            f"Powered By : {response.headers.get('X-Powered-By','Unknown')}"
        )

        html = response.text.lower()

        if "wordpress" in html:
            print("[+] WordPress Detected")

        if "php" in html:
            print("[+] PHP Detected")

        if "apache" in str(response.headers).lower():
            print("[+] Apache Server")

        if "nginx" in str(response.headers).lower():
            print("[+] Nginx Server")

    except Exception as e:

        print("Fingerprinting Failed")
        print(e)