from selenium.webdriver.common.by import By


def test_successful_login(driver):

    driver.get("https://www.saucedemo.com/")

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login_button.click()

    # Assertion 1
    assert "inventory" in driver.current_url

    # Assertion 2
    products = driver.find_element(
        By.CLASS_NAME,
        "title"
    )

    assert products.text == "Products"