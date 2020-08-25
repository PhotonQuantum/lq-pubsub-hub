from os import environ
from .models.config import GlobalConfig

CONFIG_FILE = environ["CONFIG_FILE"]
config = GlobalConfig.parse_file(CONFIG_FILE)