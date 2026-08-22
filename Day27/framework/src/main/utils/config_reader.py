import configparser
import os


class ConfigReader:

    def __init__(self):

        # Find framework root directory
        current_file = os.path.abspath(__file__)

        # src/main/utils/config_reader.py
        # -> utils
        # -> main
        # -> src
        # -> framework
        framework_root = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(current_file)
                )
            )
        )

        config_path = os.path.join(
            framework_root,
            "resources",
            "config.ini"
        )

        self.config = configparser.ConfigParser()
        self.config.read(config_path)

        if not self.config.sections():
            raise FileNotFoundError(
                f"Could not load config file: {config_path}"
            )

    def get_base_url(self):
        return self.config["environment"]["base_url"]

    def get_default_browser(self):
        return self.config["browser"]["default"]

    def get_timeout(self):
        return int(self.config["execution"]["timeout"])

    def is_headless(self):
        return self.config["execution"].getboolean("headless")