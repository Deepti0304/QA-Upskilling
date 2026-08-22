from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_home_page_displayed(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCTS_TITLE
            )
        ).is_displayed()

    def get_page_title(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.PRODUCTS_TITLE
            )
        ).text

    def open_menu(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.MENU_BUTTON
            )
        ).click()

    def logout(self):

        self.open_menu()

        self.wait.until(
            EC.element_to_be_clickable(
                self.LOGOUT_LINK
            )
        ).click()