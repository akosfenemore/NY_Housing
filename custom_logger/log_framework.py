import os.path
import json
import logging
import logging.config


class CustomLogger:

    def __init__(self):
        path = os.path.dirname(__file__) + '/log_config.json'
        if os.path.exists(path):
            with open(path, 'r') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger('mylog')


# Create logger
log = CustomLogger().logger