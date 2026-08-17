from selenium.webdriver.common.by import By


class HomePage:

    products_title = (By.CLASS_NAME, "title")
    shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.find_element(
            *self.products_title
        ).text

    def click_cart(self):
        self.driver.find_element(
            *self.shopping_cart
        ).click()

    def open_menu(self):
        self.driver.find_element(
            *self.menu_button
        ).click()

    def logout(self):
        self.open_menu()

        self.driver.find_element(
            *self.logout_link
        ).click()