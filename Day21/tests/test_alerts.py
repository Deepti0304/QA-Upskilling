from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_javascript_alert(driver):

    driver.get(
        "https://the-internet.herokuapp.com/javascript_alerts"
    )

    button = driver.find_element(
        By.XPATH,
        "//button[contains(text(),'JS Alert')]"
    )

    button.click()

    alert = WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    assert "I am a JS Alert" in alert.text

    alert.accept()

    result = driver.find_element(
        By.ID,
        "result"
    )

    assert "You successfully clicked an alert" in result.text