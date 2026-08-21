import allure

from src.main.pages.login_page import LoginPage
from src.main.pages.home_page import HomePage
from src.main.utils.config_reader import ConfigReader


@allure.feature("Navigation")
@allure.story("Browser Navigation")
def test_navigation(driver):

    config = ConfigReader()

    driver.get(config.get_base_url())

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page = HomePage(driver)

    assert home_page.is_home_page_displayed()

    with allure.step("Navigate back"):

        driver.back()

    with allure.step("Navigate forward"):

        driver.forward()

    assert home_page.is_home_page_displayed()