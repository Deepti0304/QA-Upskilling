from selenium.webdriver.common.by import By


def test_element_state(driver):

    driver.get(
        "https://www.saucedemo.com/"
    )

    username = driver.find_element(
        By.ID,
        "user-name"
    )

    assert username.is_displayed()

    assert username.is_enabled()