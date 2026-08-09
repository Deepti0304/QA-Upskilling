from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_drag_and_drop():

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.maximize_window()

        driver.get("https://jqueryui.com/droppable/")

        iframe = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".demo-frame")
            )
        )

        driver.switch_to.frame(iframe)

        source = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "draggable")
            )
        )

        target = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "droppable")
            )
        )

        actions = ActionChains(driver)

        actions.drag_and_drop(source, target).perform()

        message = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#droppable p")
            )
        )

        print("Drop message:", message.text)

        assert message.text == "Dropped!"

        driver.switch_to.default_content()

        print("Drag and drop successful")

    finally:
        driver.quit()