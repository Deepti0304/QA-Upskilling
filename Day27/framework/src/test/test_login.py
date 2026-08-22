import pytest

from src.main.pages.login_page import LoginPage


@pytest.mark.parametrize(
    "driver",
    ["chrome", "firefox", "edge"],
    indirect=True
)
def test_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert "inventory" in driver.current_url