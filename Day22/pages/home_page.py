from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    TITLE = (By.CLASS_NAME, "title")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):

        title = self.wait.until(
            EC.visibility_of_element_located(self.TITLE)
        )

        return title.text

    def open_menu(self):

        menu = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )

        menu.click()

    def open_cart(self):

        cart = self.wait.until(
            EC.element_to_be_clickable(self.CART)
        )

        cart.click()