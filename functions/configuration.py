from config import header, print, warning
from os import path
from json import loads, dumps


class Config(object):

    def __init__(self):
        file = path.abspath(__file__)
        file = file.split("/")[:2]
        self.file = path.join("/".join(file), "/", "config.json")

    def write_config(self) -> None:
        pass

    def parse_config(self) -> dict:
        try:
            config_file = open(self.file, "r")
            return loads(config_file.read())
        except FileNotFoundError:
            warning("No Config File Found, Making One")
            self.write_config()
