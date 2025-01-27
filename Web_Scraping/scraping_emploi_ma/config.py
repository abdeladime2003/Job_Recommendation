# config.py

import logging
from logging.handlers import RotatingFileHandler

#  Chemin du fichier de log
LOG_FILE_PATH = "./logs/Scraping_emploi.log"

#  Configuration de la rotation des logs
log_handler = RotatingFileHandler(
    LOG_FILE_PATH,      # Chemin du fichier de log
    maxBytes=5 * 1024 * 1024,  # Taille max = 5 Mo
    backupCount=3       # Nombre de sauvegardes : scraping.log.1, .2, .3
)

#  Format des logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

#  Configuration du logger principal
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Capture tous les niveaux
logger.addHandler(log_handler)

#  Paramètres de scraping
BASE_URL = "https://www.emploi.ma/recherche-jobs-maroc"
API_URL = "http://localhost:8000//api/add-job-offer/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0'
}

CSV_FILE_PATH = "./data/job_listings.csv"
