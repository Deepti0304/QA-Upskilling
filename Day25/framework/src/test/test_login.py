from pathlib import Path

import pytest
import allure

from src.main.pages.login_page import LoginPage
from src.main.pages.home_page import HomePage
from src.main.utils.config_reader import ConfigReader
from src.main.utils.data_reader import DataReader


BASE_DIR = Path(__file__).resolve().parents[2]

DATA_FILE = BASE_DIR / "data" / "login_data.json"

data = DataReader.read_json(DATA_FILE)


@allure.feature("Login")
@allure.story("Data Driven Login")
@pytest.mark.parametrize("test_data", data)
def test_login(driver, test_data):

    config = ConfigReader()

    driver.get(config.get_base_url())

    login_page = LoginPage(driver)

    with allure.step(
        f"Execute: {test_data['test_case']}"
    ):

        login_page.login(
            test_data["username"],
            test_data["password"]
        )

    if test_data["expected_result"] == "pass":

        home_page = HomePage(driver)

        with allure.step("Verify successful login"):

            assert home_page.is_home_page_displayed()

    else:

        with allure.step("Verify login failure"):

            assert login_page.get_error_message()