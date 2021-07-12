from collections import namedtuple
import json
import os

KeyboardCommandMapper = namedtuple("KeyboardEventMapper", "initialize, pause, finish")

ROOT_PATH = os.getcwd()
CONFIG_FILE = "command_config.json"
CONFIG_PATH = os.path.join(ROOT_PATH, CONFIG_FILE)

with open(CONFIG_PATH, "r") as file:
    content = file.read()
    config = json.loads(content)
    key_mapper = KeyboardCommandMapper(**config)
