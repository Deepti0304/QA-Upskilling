class ChromeDriver:

    def start(self):
        print("Launching Chrome Browser")


class FirefoxDriver:

    def start(self):
        print("Launching Firefox Browser")


class DriverFactory:

    @staticmethod
    def get_driver(browser):

        if browser.lower() == "chrome":
            return ChromeDriver()

        elif browser.lower() == "firefox":
            return FirefoxDriver()

        else:
            raise ValueError("Unsupported Browser")