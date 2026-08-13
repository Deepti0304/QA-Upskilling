def test_cookies(driver):

    driver.get(
        "https://the-internet.herokuapp.com/"
    )

    driver.add_cookie({
        "name": "automation",
        "value": "selenium"
    })

    cookie = driver.get_cookie(
        "automation"
    )

    assert cookie is not None

    assert cookie["value"] == "selenium"