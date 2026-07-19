from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():

    driver = webdriver.Chrome()

    try:

        driver.maximize_window()

        driver.get("https://www.saucedemo.com/")

        # Username (ID)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")

        # Password (Name)
        driver.find_element(By.NAME, "password").send_keys("secret_sauce")

        # Login Button (ID)
        driver.find_element(By.ID, "login-button").click()

        # Verify successful login
        assert "inventory" in driver.current_url

        print("Login Successful")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_login()