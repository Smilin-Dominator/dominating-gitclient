from config import header, print, warning
from pathlib import Path
from json import loads, dumps


class Config(object):

    def __init__(self):
        file = __file__[:-27]
        self.file = Path(file, "config.json")

    def write_config(self) -> None:
        config = self.WriteJSON()
        config.__add__("field1", "a")
        config.__add__("field2", "b")
        config.__add__("field3", "c")
        config_file = open(self.file, "w+")
        json_dump = dumps(config.__get__(), indent=4)
        config_file.write(json_dump)
        config_file.flush()
        config_file.close()

    def parse_config(self) -> dict:
        try:
            config_file = open(self.file, "r")
            return loads(config_file.read())
        except FileNotFoundError:
            warning("No Config File Found, Making One")
            self.write_config()

    class WriteJSON(object):

        def __init__(self):
            self.config = {}

        def __add__(self, field: str, value):
            self.config[field] = value

        def __get__(self):
            return self.config
