from selenium import webdriver
from selenium.webdriver.common.by import By


def test_js_executor():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/large")

        # --------------------------------
        # 1. Scroll to the bottom
        # --------------------------------

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        print("Scrolled to bottom")

        # --------------------------------
        # 2. Scroll to a specific element
        # --------------------------------

        element = driver.find_element(By.ID, "page-footer")

        driver.execute_script(
            "arguments[0].scrollIntoView();",
            element
        )

        assert element.is_displayed()

        print("Element is visible:", element.is_displayed())

        # --------------------------------
        # 3. Read an element property
        # --------------------------------

        tag_name = driver.execute_script(
            "return arguments[0].tagName;",
            element
        )

        print("Tag name:", tag_name)

        assert tag_name == "DIV"

        # --------------------------------
        # 4. JavaScript click
        # --------------------------------

        driver.execute_script(
            "arguments[0].click();",
            element
        )

        print("JavaScript click executed")

    finally:
        driver.quit()