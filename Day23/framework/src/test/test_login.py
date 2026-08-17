from src.test.base_test import BaseTest
from src.main.pages.login_page import LoginPage
from src.main.utils.config_reader import ConfigReader


class TestLogin(BaseTest):

    def test_login(self):

        config = ConfigReader()

        self.driver.get(
            config.get_base_url()
        )

        login_page = LoginPage(self.driver)

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        assert "inventory" in self.driver.current_url