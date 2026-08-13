import os

def test_screenshot(driver):

    driver.get(
        "https://the-internet.herokuapp.com/"
    )

    os.makedirs(
        "Day21/screenshots",
        exist_ok=True
    )

    file_path = (
        "Day21/screenshots/homepage.png"
    )

    result = driver.save_screenshot(file_path)

    assert result is True

    assert os.path.exists(file_path)