from pages.login_page import LoginPage
from pages.home_page import HomePage


def test_successful_login(driver):

    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page = HomePage(driver)

    assert home_page.get_title() == "Products"