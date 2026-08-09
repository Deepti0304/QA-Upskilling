from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_hover_menu():

    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/hovers")

        user = driver.find_element(By.XPATH, "(//div[@class='figure'])[1]")

        actions = ActionChains(driver)

        actions.move_to_element(user).perform()

        caption = driver.find_element(
            By.XPATH,
            "(//div[@class='figcaption'])[1]"
        )

        print("Caption:", caption.text)

        assert caption.is_displayed()

    finally:
        driver.quit()