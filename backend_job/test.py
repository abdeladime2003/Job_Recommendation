import json 
import requests
import time
"""envoyer ca {'titre': 'Directeur(trice) médical(e) - DIRECTION DES AFFAIRES MEDICALES', 'entreprise': "HUIR - L'Hôpital Universitaire International de Rabat", 'description': 'Manager la Direction des affaires médicales : • Manager les équipes de la direction et des directeurs de spécialités médicales : organisation, motivation et évaluation • Assurer le pilotage de...', 'localisation': 'Rabat (Maroc)', 'date_publication': '16.01.2025', 'date_limite': '16.03.2025', 'nombre_postes': 'Postes proposés: 1', 'niveau_experience': 'De 10 à 20 ans', 'niveau_etudes_requis': 'Bac +5 et plus', 'competences_cles': ['Médical ', ' Paramédical'], 'contrat_propose': 'CDI', 'teletravail': 'Non', 'lien': 'https://www.rekrute.com/offre-emploi-directeurtrice-medicale---direction-des-affaires-medicales-recrutement-huir---lhopital-universitaire-international-de-rabat-rabat-167763.html'}

"""
response = requests.post("http://localhost:8000//api/add-job-offer/", json={
    'titre': 'Directeur(trice) médical(e) - DIRECTION DES AFFAIRES MEDICALES', 
    'entreprise': "HUIR - L'Hôpital Universitaire International de Rabat", 
    'description': 'Manager la Direction des affaires médicales : • Manager les équipes de la direction et des directeurs de spécialités médicales : organisation, motivation et évaluation • Assurer le pilotage de...',

    'localisation': 'Rabat (Maroc)',
    'date_publication': '16.01.2025',
    'date_limite': '16.03.2025',
    'nombre_postes': 'Postes proposés: 1',
    'niveau_experience': 'De 10 à 20 ans',
    'niveau_etudes_requis': 'Bac +5 et plus',
    'competences_cles': ['Médical ', ' Paramédical'],
    'contrat_propose': 'CDI',
    'teletravail': 'Non',
    'lien': 'https://www.rekrute.com/offre-emploi-directeurtrice-medicale---direction-des-affaires-medicales-recrutement-huir---lhopital-universitaire-international-de-rabat-rabat-167763.html'

})
## print error if there is any
print(response.json())
print(response.status_code)
print(response.headers)
print(response.text)
print(response.url)
print(response.request)
print(response.request.body)
