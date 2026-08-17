import configparser
import os


class ConfigReader:

    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(__file__),
            "../../../resources/config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_base_url(self):
        return self.config["environment"]["base_url"]

    def get_browser(self):
        return self.config["settings"]["browser"]

    def get_timeout(self):
        return int(self.config["settings"]["timeout"])


config = ConfigReader()

url = config.get_base_url()
browser = config.get_browser()
timeout = config.get_timeout()