def lookup_cves(banner):

    banner = banner.lower()

    cves = []

    if "openssh" in banner:
        cves.append(("CVE-2016-0777", "HIGH"))
        cves.append(("CVE-2015-5600", "MEDIUM"))

    if "apache" in banner:
        cves.append(("CVE-2021-41773", "HIGH"))
        cves.append(("CVE-2021-42013", "CRITICAL"))

    return cves