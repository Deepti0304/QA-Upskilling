import pytest
from selenium import webdriver

from src.main.utils.failure_handler import FailureHandler


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            FailureHandler.capture(
                driver,
                item.name
            )