# config.py
# config.py

import logging

LOG_FILE_PATH = "./logs/scraping.log"

# Configuration du logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BASE_URL = "https://www.emploi.ma/recherche-jobs-maroc"
API_URL = "https://e9d8-160-178-233-248.ngrok-free.app/api/add-job-offer/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0'
}

CSV_FILE_PATH = "./data/job_listings.csv"
LOG_FILE_PATH = "./logs/scraping.log"
