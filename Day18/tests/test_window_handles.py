from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_window_handles():

    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    try:

        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/windows")

        # Store parent window
        parent = driver.current_window_handle

        print("Parent:", parent)

        # Click link
        driver.find_element(By.LINK_TEXT, "Click Here").click()

        # Get all windows
        handles = driver.window_handles

        print(handles)

        # Switch to child
        for handle in handles:

            if handle != parent:

                driver.switch_to.window(handle)

                break

        heading = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h3"))
        )

        assert heading.text == "New Window"

        print("Child validated")

        # Close child
        driver.close()

        # Back to parent
        driver.switch_to.window(parent)

        heading = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h3"))
        )

        assert heading.text == "Opening a new window"

        print("Parent validated")

    finally:

        driver.quit()