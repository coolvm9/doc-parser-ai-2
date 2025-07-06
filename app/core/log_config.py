import logging.config
import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'log_config.yaml')

_logging_configured = False

def setup_logging():
    global _logging_configured
    if not _logging_configured:
        with open(CONFIG_PATH, 'r') as f:
            config = yaml.safe_load(f)
        logging.config.dictConfig(config)
        _logging_configured = True

def get_logger(name=None):
    if not _logging_configured:
        setup_logging()
    return logging.getLogger(name or 'myapp')
