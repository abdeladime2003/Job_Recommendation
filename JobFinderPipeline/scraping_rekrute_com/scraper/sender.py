import requests
import logging
API_URL = "http://localhost:8000//api/add-job-offer/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0'
}

class Sender:
    def __init__(self, api_url=API_URL, headers=HEADERS):
        self.api_url = api_url
        self.headers = headers
        self.session = requests.Session()  # Utilisation d'une session pour des requêtes plus performantes
        self.session.headers.update(self.headers)

    def send(self, data):
        """
        Envoie les données à l'API via des requêtes POST.
        
        :param data: Liste de dictionnaires contenant les offres à envoyer.
        """
        if not data:
            logging.warning("Aucune donnée à envoyer.")
            return

        for index, entry in enumerate(data, start=1):
            try:
                response = self.session.post(self.api_url, json=entry, timeout=10)
                response.raise_for_status()
                logging.info(f"[{index}] Envoi réussi : {response.status_code} - {response.json()}")
            except requests.exceptions.HTTPError as http_err:
                logging.error(f"[{index}] Erreur HTTP : {http_err} - Donnée : {entry}")
            except requests.exceptions.ConnectionError as conn_err:
                logging.error(f"[{index}] Erreur de connexion : {conn_err}")
            except requests.exceptions.Timeout as timeout_err:
                logging.error(f"[{index}] Délai d'attente dépassé : {timeout_err}")
            except requests.RequestException as err:
                logging.error(f"[{index}] Erreur inattendue : {err}")
            except Exception as e:
                logging.error(f"[{index}] Exception inconnue : {e}")

    def close_session(self):
        """Ferme proprement la session HTTP."""
        self.session.close()
