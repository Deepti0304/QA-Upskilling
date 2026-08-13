from selenium.webdriver.common.by import By
import time


def test_multiple_windows(driver):

    driver.get(
        "https://the-internet.herokuapp.com/windows"
    )

    parent_window = driver.current_window_handle

    driver.find_element(
        By.LINK_TEXT,
        "Click Here"
    ).click()

    time.sleep(1)

    windows = driver.window_handles

    assert len(windows) == 2

    for window in windows:

        if window != parent_window:

            driver.switch_to.window(window)

            break

    assert "New Window" in driver.page_source

    driver.close()

    driver.switch_to.window(parent_window)

    assert "The Internet" in driver.title