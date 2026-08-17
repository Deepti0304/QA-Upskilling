import pytest
from selenium import webdriver

from src.main.utils.config_reader import ConfigReader


class BaseTest:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):

        config = ConfigReader()

        browser = config.get_browser()

        if browser.lower() == "chrome":
            self.driver = webdriver.Chrome()

        elif browser.lower() == "firefox":
            self.driver = webdriver.Firefox()

        else:
            raise ValueError(
                f"Unsupported browser: {browser}"
            )

        self.driver.maximize_window()

        yield

        self.driver.quit()