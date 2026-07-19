from selenium import webdriver
from selenium.webdriver.common.by import By


def test_advanced_locators():

    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        driver.get("https://demoqa.com/text-box")

        # CSS Selector
        driver.find_element(By.CSS_SELECTOR, "#userName").send_keys("Deepti")

        driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("deepti@test.com")

        # XPath
        driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys(
            "Hyderabad"
        )

        driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys(
            "India"
        )

        driver.find_element(By.CSS_SELECTOR, "#submit").click()

        assert "text-box" in driver.current_url

    finally:
        driver.quit()