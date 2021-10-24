import sys
import logging
from ..settings import settings


class Logger:  # pylint: disable=unused-private-member

    __instance = None

    @staticmethod
    def instance():
        if Logger.__instance is None:
            Logger()
        return Logger.__instance

    def __init__(self):
        if Logger.__instance is not None:
            raise Exception("You must invoke Logger.instance()")

        Logger._log_settings()

        Logger.__instance = self

    @staticmethod
    def _log_settings():

        logger_params = {
            'format': settings.logger_config['log_format'],
            'datefmt': settings.logger_config['date_format']
        }

        log_file = settings.logger_config['log_file']

        if log_file:
            logger_params['filename'] = log_file
        else:
            logger_params['stream'] = sys.stdout

        logging.basicConfig(**logger_params)

        logger = logging.getLogger()
        logger.disabled = settings.logger_config['disabled']
        logger.level = settings.logger_config['level']

    @staticmethod
    def disable():
        logging.getLogger().disabled = True

    @staticmethod
    def enable():
        logging.getLogger().disabled = False

    @property
    def level(self):
        return logging.getLogger().level

    @level.setter
    def level(self, level):  # pylint: disable=no-self-use
        logging.getLogger().setLevel(level)

    @property
    def disabled(self):
        return logging.getLogger().disabled
