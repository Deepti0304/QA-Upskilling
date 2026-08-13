from selenium.webdriver.common.by import By


def test_google_search(driver):

    query = "Selenium Python"

    #driver.get("https://www.google.com")
    driver.get("https://search.brave.com/?lang=en-in")


    search_box = driver.find_element(
        By.NAME,
        "q"
    )

    search_box.send_keys(query)
    search_box.submit()

    assert query.lower() in driver.title.lower()