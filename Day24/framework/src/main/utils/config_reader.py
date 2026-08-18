import configparser
import os


class ConfigReader:

    def __init__(self):

        self.config = configparser.ConfigParser()

        config_path = os.path.join(
            os.path.dirname(__file__),
            "../../../config/config.ini"
        )

        self.config.read(config_path)

    def get_base_url(self):

        return self.config["environment"]["base_url"]

    def get_browser(self):

        return self.config["environment"]["browser"]