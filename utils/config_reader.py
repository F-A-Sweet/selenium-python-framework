import json


class ConfigReader:

    @staticmethod
    def get_config():
        with open("config/config.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_base_url():
        return ConfigReader.get_config()["base_url"]

    @staticmethod
    def get_browser():
        return ConfigReader.get_config()["browser"]

    @staticmethod
    def get_implicit_wait():
        return ConfigReader.get_config()["implicit_wait"]