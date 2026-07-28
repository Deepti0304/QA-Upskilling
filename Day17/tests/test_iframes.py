from selenium import webdriver
from selenium.webdriver.common.by import By


def test_nested_frames():
    driver = webdriver.Chrome()

    try:
        driver.maximize_window()

        driver.get("https://the-internet.herokuapp.com/nested_frames")

        # Top frame
        driver.switch_to.frame("frame-top")

        # Left frame
        driver.switch_to.frame("frame-left")
        print(driver.find_element(By.TAG_NAME, "body").text)

        driver.switch_to.parent_frame()

        # Middle frame
        driver.switch_to.frame("frame-middle")
        print(driver.find_element(By.ID, "content").text)

        driver.switch_to.parent_frame()

        # Right frame
        driver.switch_to.frame("frame-right")
        print(driver.find_element(By.TAG_NAME, "body").text)

        # Back to main page
        driver.switch_to.default_content()

        # Bottom frame
        driver.switch_to.frame("frame-bottom")
        print(driver.find_element(By.TAG_NAME, "body").text)

    finally:
        driver.quit()