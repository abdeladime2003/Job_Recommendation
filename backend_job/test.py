import csv
import json
import requests
def csv_to_json_and_send(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:

            if isinstance(row['comptence'], str):
                try:
                    row['comptence'] = json.loads(row['comptence']) 
                except json.JSONDecodeError:
                    row['comptence'] = [] 
            send(row)

def send(data):
    try:

        response = requests.post("https://719d-105-155-133-97.ngrok-free.app/api/add-job-offer/", json=data)
     
        print(response.json())


        response.raise_for_status()
        print(f"Envoi réussi: {response.status_code}")
    except requests.RequestException as e:
        print(f"Erreur lors de l'envoi des données: {e}")

if __name__ == "__main__":
    csv_file_path = r'C:\Users\LENOVO\Downloads\Prod.csv' 
    

    csv_to_json_and_send(csv_file_path)
