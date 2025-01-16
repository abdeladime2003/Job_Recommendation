import logging.config
from pythonjsonlogger import jsonlogger

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",  # Handler for writing logs to a file
            "filename": "Anapec/logs/app.log",          # Log file name
            "formatter": "json",           # Use the JSON formatter
        },
        "console": {
            "class": "logging.StreamHandler",  # Handler for writing logs to console
            "stream": "ext://sys.stdout",  # Stream logs to standard output
            "formatter": "json",  # Use the JSON formatter
            "level": "INFO",  # Minimum log level to capture in console
        },
        
    },
    "loggers": {
        "": {
            "handlers": ["file","console"],  # Logs will go to both the file and console
            "level": "INFO",               # Minimum log level to capture
        }
    },
}


logging.config.dictConfig(LOGGING)

Site = 'https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg=1'
endpoint = "https://e9d8-160-178-233-248.ngrok-free.app/api/add-job-offer/"
driverPath = "Anapec/driver/geckodriver.exe"
csvPath = "Anapec/data/Prod.csv"