import pytest
import allure

from src.main.pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Data Driven Login")
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("invalid_user", "wrong_password")
    ]
)
def test_login(driver, username, password):

    login_page = LoginPage(driver)

    login_page.login(username, password)