import pytest

from src.main.pages.login_page import LoginPage
from src.main.utils.data_reader import DataReader
from src.main.utils.config_reader import ConfigReader


# Read CSV test data
data = DataReader.read_csv("data/login_data.csv")

# Read configuration
config = ConfigReader()


@pytest.mark.parametrize("test_data", data)
def test_login_csv(driver, test_data):

    # Open application using URL from config.ini
    driver.get(config.get_base_url())

    # Create Login Page object
    login_page = LoginPage(driver)

    # Perform login
    login_page.login(
        test_data["username"],
        test_data["password"]
    )

    # Validate result
    if test_data["expected_result"] == "success":

        assert "inventory" in driver.current_url

    else:

        assert "inventory" not in driver.current_url