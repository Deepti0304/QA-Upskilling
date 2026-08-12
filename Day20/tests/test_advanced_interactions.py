from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_advanced_interactions():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        # Create screenshots directory
        screenshot_dir = "Day20/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # -----------------------------------
        # 1. Open application
        # -----------------------------------

        driver.get("https://the-internet.herokuapp.com/")

        print("Page title:", driver.title)

        driver.save_screenshot(
            f"{screenshot_dir}/01_homepage.png"
        )

        # -----------------------------------
        # 2. Cookies
        # -----------------------------------

        driver.add_cookie({
            "name": "test_cookie",
            "value": "selenium123"
        })

        cookie = driver.get_cookie("test_cookie")

        print("Cookie:", cookie)

        assert cookie is not None
        assert cookie["value"] == "selenium123"

        driver.save_screenshot(
            f"{screenshot_dir}/02_cookie.png"
        )

        # -----------------------------------
        # 3. File Upload
        # -----------------------------------

        driver.get(
            "https://the-internet.herokuapp.com/upload"
        )

        upload = driver.find_element(
            By.ID,
            "file-upload"
        )

        file_path = os.path.abspath(
            "Day20/sample.txt"
        )

        upload.send_keys(file_path)

        driver.save_screenshot(
            f"{screenshot_dir}/03_file_upload.png"
        )

        print("File uploaded successfully")

        # -----------------------------------
        # 4. Shadow DOM
        # -----------------------------------

        driver.get(
            "https://shop.polymer-project.org/"
        )

        driver.save_screenshot(
            f"{screenshot_dir}/04_shadow_dom.png"
        )

        print("Shadow DOM page opened")

    finally:

        driver.quit()