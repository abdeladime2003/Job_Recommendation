import requests

class Sender:
    def __init__(self, api_url):
        self.api_url = api_url

    def send(self, data):
        try:
            response = requests.post("https://b8c4-105-155-240-10.ngrok-free.app/api/add-job-offer/", json=data)
            print(response.json())

            response.raise_for_status()
            print(f"Envoi réussi: {response.status_code}")
        except requests.RequestException as e:
            print(f"Erreur lors de l'envoi des données: {e}")
