import os
import logging
from logging.handlers import RotatingFileHandler



def setup_logging(log_file_path: str, file_log_level: int = logging.ERROR, console_log_level: int = logging.INFO) -> None:
    """
    Set up a centralized logging configuration with rotating file handler.
    
    :param log_file_path: Path to the log file
    :param file_log_level: Logging level for file handler
    :param console_log_level: Logging level for console handler
    """
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.handlers.clear()

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler = RotatingFileHandler(
        log_file_path, 
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(file_log_level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(console_log_level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)