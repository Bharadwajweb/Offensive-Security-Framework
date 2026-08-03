import requests

def directory_scan(target):

    print("\n" + "=" * 60)
    print("DIRECTORY DISCOVERY MODULE")
    print("=" * 60)

    try:

        with open("wordlist.txt", "r") as f:

            paths = f.readlines()

        for path in paths:

            path = path.strip()

            url = f"http://{target}{path}"

            try:

                r = requests.get(url, timeout=2)

                if r.status_code < 400:

                    print(f"[FOUND] {url}")

            except:
                pass

    except:

        print("Wordlist Missing")