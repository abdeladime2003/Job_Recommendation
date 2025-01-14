import requests

job_offer = {
    "lieu": "Rabddddt",
    "description": "DATA ENGINEER ",
    "date_publication": "2024-01-13",
    "type": "Full-time",
    "competences_requises": ["Python", "Django", "MongoDB"],
    "lien_postulation": "https://INPT.ma",
}

response = requests.post("https://89a2-196-92-162-121.ngrok-free.app/api/add-job-offer/", json=job_offer)
print(response.json())
