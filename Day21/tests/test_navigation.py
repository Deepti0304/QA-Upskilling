from selenium import webdriver


def test_browser_navigation():

    driver = webdriver.Chrome()

    try:
        # 1. Open Google
        driver.get("https://www.google.com")
        assert "google" in driver.current_url.lower()

        # 2. Open Wikipedia
        driver.get("https://www.wikipedia.org")
        assert "wikipedia" in driver.current_url.lower()

        # 3. Go back to Google
        driver.back()
        assert "google" in driver.current_url.lower()

        # 4. Go forward to Wikipedia
        driver.forward()
        assert "wikipedia" in driver.current_url.lower()

        # 5. Refresh
        driver.refresh()
        assert "wikipedia" in driver.current_url.lower()

        print("Browser navigation test passed")

    finally:
        driver.quit()