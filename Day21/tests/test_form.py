from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_practice_form(driver):

    driver.get(
        "https://demoqa.com/automation-practice-form"
    )

    wait = WebDriverWait(driver, 10)

    first_name = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "firstName")
        )
    )

    first_name.send_keys("Deepti")

    assert first_name.get_attribute("value") == "Deepti"

    last_name = driver.find_element(
        By.ID,
        "lastName"
    )

    last_name.send_keys("Patel")

    assert last_name.get_attribute("value") == "Patel"