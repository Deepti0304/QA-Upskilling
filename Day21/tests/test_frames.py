from selenium.webdriver.common.by import By


def test_iframe(driver):

    driver.get(
        "https://the-internet.herokuapp.com/iframe"
    )

    frame = driver.find_element(
        By.ID,
        "mce_0_ifr"
    )

    driver.switch_to.frame(frame)

    body = driver.find_element(
        By.ID,
        "tinymce"
    )

    assert body.is_displayed()

    driver.switch_to.default_content()

    heading = driver.find_element(
        By.TAG_NAME,
        "h3"
    )

    assert heading.text == "An iFrame containing the TinyMCE WYSIWYG Editor"