import configparser
from pathlib import Path


class ConfigReader:

    def __init__(self):

        config_path = (
            Path(__file__).resolve()
            .parents[3]
            / "resources"
            / "config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

    def get_base_url(self):

        return self.config["environment"]["base_url"]

    def get_browser(self):

        return self.config["browser"]["name"]