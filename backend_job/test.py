import requests

job_offer = {
    "lieu": "Rabddddt",
    "description": "DATA ENGINEER ",
    "date_publication": "2024-01-13",
    "type": "Full-time",
    "competences_requises": ["Python", "Django", "MongoDB"],
    "lien_postulation": "https://INPT.ma",
}

response = requests.post("https://b8c4-105-155-240-10.ngrok-free.app/api/add-job-offer/", json=job_offer)
print(response.json())
