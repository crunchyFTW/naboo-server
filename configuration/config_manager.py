import json
import logging
import os
from json import JSONDecodeError

import yaml

from tools.deep_copy import json_deep_update
from tools.singeltone import Singleton


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


class Configuration(metaclass=Singleton):
    NABOO_ENV_VARIABLE = "SOUNDIFY_ENV"
    DEFAULT_CONFIG_NAME = "develop"


    def __init__(self):
        self._config_name: str = self.__get_config_name()
        self._config: dict = self.__load_configuration(self._config_name)


    def __get_config_name(self):
        config_file_name = os.environ.get(self.NABOO_ENV_VARIABLE, self.DEFAULT_CONFIG_NAME)
        return f"{config_file_name}.yaml"


    def __load_configuration(self, config_file_name: str):
        def _get_config_paths(config_file_name: str):
            cur_dir = os.getcwd()
            config_file_paths = [
                f"{os.path.join(cur_dir, config_file_name)}",
                f"{os.path.join(os.path.join(cur_dir, 'configuration'), config_file_name)}",
                f"{os.path.join(os.path.join(cur_dir, '..'), config_file_name)}",
                f"{os.path.join(os.path.expanduser('~'), config_file_name)}",
                f"{os.path.join('/etc/soundify', config_file_name)}",
            ]
            return config_file_paths


        config_file_paths = _get_config_paths(config_file_name)

        for c_f_p in config_file_paths:
            logger.info(f"trying to load config : {c_f_p}")
            if not os.path.exists(c_f_p):
                continue

            logger.info(f"loading config : {c_f_p}")
            with open(c_f_p, "r") as f:
                config: dict = yaml.safe_load(f)
            try:
                new_config_data = json.loads(os.environ.get("SOUNDIFY_SET", "{}"))
            except JSONDecodeError as e:
                logger.error(f"new config data is not in right format")
                raise e
            json_deep_update(config, new_config_data)
            return config

        logger.error(f"Configuration could not be found")
        raise IOError(f"Configuration could not be found")


    def get(self, section: str = None):
        if section:
            return self._config.get(section, {})
        return self._config