import json 
import requests
import time
"""envoyer ca {
    "titre": "Développeur Python",
    "entreprise": "TechCorp",
    "localisation": "Casablanca",
    "description": "Nous recherchons un développeur Python...",
    "competences_cles": ["Python", "Django", "API"],
    "niveau_etudes_requis": "Bac+3",
    "niveau_experience": "2 ans",
    "contrat_propose": "CDI",
    "date_publication": "15.01.2025",
    "lien": "https://example.com/offre"
}
"""
response = requests.post("https://e9d8-160-178-233-248.ngrok-free.app/api/add-job-offer/", json={
    "titre": "Développeur Python",
    "entreprise": "TechCorp",
    "localisation": "Casablanca",
    "description": "Nous recherchons un développeur Python...",
    "competences_cles": ["Python", "Django", "API"],
    "niveau_etudes_requis": "Bac+3",
    "niveau_experience": "2 ans",
    "contrat_propose": "CDI",
    "date_publication": "15.01.2025",
    "lien": "https://example.com/offre"
})
print(response.status_code)