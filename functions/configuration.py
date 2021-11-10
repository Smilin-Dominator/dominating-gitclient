from config import print, input, warning
from pathlib import Path
from json import loads, dumps


class Config(object):

    def __init__(self):
        file = __file__[:-27]
        self.file = Path(file, "config.json")

    def write_config(self) -> None:
        config = self.WriteJSON()

        choice = int(input("\tCheck For Updates? (Per x Boot, 0 for Never)", default="4", choices=["0", "1", "2", "3", "4"], override="tan"))
        config.__add__("update_check_frequency", choice)

        choice = input("\tDefault Directory (goes here if no args are given)", override="orange1")
        config.__add__("default_dir", choice)

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
