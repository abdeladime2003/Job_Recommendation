# scraper/sender.py

import requests
import logging
from config import API_URL

class Sender:
    def __init__(self, api_url=API_URL):
        self.api_url = api_url

    def send(self, data):
        for entry in data:
            try:
                response = requests.post(self.api_url, json=entry)
                response.raise_for_status()
                logging.info(f"Envoi réussi : {response.status_code} - {entry['titre']}")
            except requests.RequestException as e:
                logging.error(f"Erreur lors de l'envoi des données : {e}")
