import logging
import os
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
LOG_FILE_PATH = "./logs_cv.log"
file_handler = logging.FileHandler(LOG_FILE_PATH)
logger.addHandler(file_handler)
