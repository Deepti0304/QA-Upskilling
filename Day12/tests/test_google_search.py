from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.chrome.options import Options

# options = Options()

# options.add_argument("--start-maximized")

# Reduce automation detection
# options.add_experimental_option(
#     "excludeSwitches",
#     ["enable-automation"]
# )

# options.add_experimental_option(
#     "useAutomationExtension",
#     False
# )


def test_google_search():
    driver = webdriver.Firefox()

    try:
        driver.maximize_window()
        driver.get("https://www.google.com")

        search_box = driver.find_element(By.NAME, 'q')
        query = "Selenium Python"
        # search_box.send_keys(query)
        for ch in "Selenium Python":
         search_box.send_keys(ch)
         time.sleep(0.1)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)
        print("Page Title:", driver.title)
        assert query.lower() in driver.title.lower()
        print("Test Passed")

    finally:
        driver.quit()

# Running the file directly for testing
# Importing functions into other modules without executing them

if __name__ == "__main__":
    test_google_search()
