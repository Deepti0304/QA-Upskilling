import pytest

from src.main.utils.browser_factory import BrowserFactory
from src.main.utils.config_reader import ConfigReader


@pytest.fixture
def driver(request):

    browser = request.param

    driver = BrowserFactory.create_driver(browser)

    config = ConfigReader()

    driver.get(config.get_base_url())

    yield driver

    driver.quit()