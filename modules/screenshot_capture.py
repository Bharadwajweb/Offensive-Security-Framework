from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from datetime import datetime
import os

def screenshot_capture(target):

    print("\n" + "=" * 60)
    print("SCREENSHOT CAPTURE MODULE")
    print("=" * 60)

    os.makedirs("screenshots", exist_ok=True)

    filename = datetime.now().strftime(
        "screenshots/screenshot_%Y%m%d_%H%M%S.png"
    )

    service = Service("drivers/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    try:
        driver.get(f"http://{target}")
        driver.save_screenshot(filename)

        print(f"[+] Screenshot Saved : {filename}")

    except Exception as e:
        print(f"Error : {e}")

    driver.quit()
