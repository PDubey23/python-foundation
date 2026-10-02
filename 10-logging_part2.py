import logging.config

logger = logging.getLogger("my_app")

logging_config = {
    "version": 1,
    "disable_existing_logger": False,
    "formatters":{
        "simple": {
            "format": "%(levelname)s: %(message)s",
        }
    },
    "handlers": {
        "stdout": {
             "class": "Logging.StreamHandler",
             "formatter": "simple",
             "stream": "ext://sys.stdout", 
        }
    },
    "loggers": {
        "root": {"level":"DEBUG", "handlers": ["stdout"]}
    },
}

# In 16 lines we had configured what basiConfig did in one line
# keep log config in separate file either in .yml or .json
