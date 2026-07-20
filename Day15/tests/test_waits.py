from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_explicit_wait():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        driver.get("https://demoqa.com/dynamic-properties")

        wait = WebDriverWait(driver, 10)

        button = wait.until(
            EC.element_to_be_clickable((By.ID, "enableAfter"))
        )

        button.click()

        print("Button Clicked Successfully")

    finally:
        driver.quit()