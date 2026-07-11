from singleton_config import ConfigReader
from driver_factory import DriverFactory
from builder_example import UserBuilder
from login_page import LoginPage


# Singleton Demo
config1 = ConfigReader()
config2 = ConfigReader()

print("Singleton Check:", config1 is config2)

print("Environment:", config1.get_environment())


# Factory Demo
driver = DriverFactory.get_driver("chrome")
driver.start()


# Builder Demo
user = (
    UserBuilder()
    .first_name("John")
    .last_name("Smith")
    .email("john@gmail.com")
    .build()
)

print("\nUser Data:")
print(user)


# POM Demo
page = LoginPage(driver)

page.enter_username("admin")
page.enter_password("admin123")
page.click_login()