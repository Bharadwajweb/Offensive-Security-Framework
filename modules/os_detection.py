def detect_os(banner):

    banner = banner.lower()

    if "ubuntu" in banner:
        return "Linux (Ubuntu)"

    elif "openssh" in banner:
        return "Linux/Unix"

    elif "apache" in banner:
        return "Linux Web Server"

    elif "iis" in banner:
        return "Windows Server"

    elif "microsoft" in banner:
        return "Windows"

    else:
        return "Unknown"
