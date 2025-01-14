from scraper import Scraper
from converter import Converter
from sender import Sender

BASE_URL = "https://www.emploi.ma/recherche-jobs-maroc"
API_URL = "https://b8c4-105-155-240-10.ngrok-free.app/api/add-job-offer/"  # Remplacez par votre URL API

if __name__ == "__main__":
    scraper = Scraper(BASE_URL)
    converter = Converter()
    sender = Sender(API_URL)
    total_pages = 23
    batch_size = 1

    for start_page in range(0, total_pages, batch_size):
        max_pages = min(batch_size, total_pages - start_page)
        print(f"Scraping pages {start_page + 1} to {start_page + max_pages}...")
        
        job_data = scraper.scrape(max_pages=max_pages)
        print(f"Récupération de {len(job_data)} offres d'emploi.")
        if not job_data:
            print("Aucune donnée récupérée.")
            continue

        job_json = converter.to_json(job_data)
        print("Conversion des données en JSON.")
        print(job_json)
        sender.send(job_data)
        print("Envoi des données à l'API.")
        print("Batch terminé.\n")
