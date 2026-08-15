from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    MOBILE = (By.ID, "userNumber")
    SUBJECT = (By.ID, "subjectsInput")
    ADDRESS = (By.ID, "currentAddress")
    SUBMIT = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, value):

        element = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )

        element.send_keys(value)

    def enter_last_name(self, value):

        element = self.wait.until(
            EC.visibility_of_element_located(self.LAST_NAME)
        )

        element.send_keys(value)

    def enter_email(self, value):

        element = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )

        element.send_keys(value)

    def enter_mobile(self, value):

        element = self.wait.until(
            EC.visibility_of_element_located(self.MOBILE)
        )

        element.send_keys(value)

    def enter_address(self, value):

        element = self.wait.until(
            EC.visibility_of_element_located(self.ADDRESS)
        )

        element.send_keys(value)

    def click_submit(self):

        submit = self.wait.until(
            EC.element_to_be_clickable(self.SUBMIT)
        )

        submit.click()