from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_javascript_alerts():
    driver = webdriver.Chrome()

    try:
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/javascript_alerts")

        # Simple Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

        alert = wait.until(EC.alert_is_present())

        print("Alert Text:", alert.text)

        assert alert.text == "I am a JS Alert"

        alert.accept()

        result = driver.find_element(By.ID, "result").text

        assert "You successfully clicked an alert" in result

        # Confirmation Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

        alert = wait.until(EC.alert_is_present())

        alert.dismiss()

        result = driver.find_element(By.ID, "result").text

        assert "Cancel" in result

        # Prompt Alert
        driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

        alert = wait.until(EC.alert_is_present())

        alert.send_keys("Deepti")

        alert.accept()

        result = driver.find_element(By.ID, "result").text

        assert "Deepti" in result

    finally:
        driver.quit()