import requests
from bs4 import BeautifulSoup
import time
import csv
class Scraper:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers or {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

        }
    
    def scrape(self, max_pages=3):
        job_listings = []

        for page in range(1, max_pages + 1):
            url = f"{self.base_url}?page={page}"
            print(f"Scraping page: {url}")
            
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"Erreur lors de l'accès à {url}: {e}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            offers = soup.find_all("div", class_="card-job-detail")

            if not offers:
                print("Aucune offre trouvée.")
                continue

            for offer in offers:
                title_tag = offer.find("h3").find("a")
                title = title_tag.text.strip() if title_tag else "N/A"
                link = f"https://www.emploi.ma{title_tag.get('href')}" if title_tag else "N/A"

                company = offer.find("h3").text.strip() if offer.find("h3") else "N.C."
                location = "N/A"
                for li in offer.find_all("li"):
                    if "Région de" in li.text:
                        location = li.find("strong").text.strip() if li.find("strong") else li.text.strip()
                skills = "N/A"
                for li in offer.find_all("li"):
                    if "Compétences clés" in li.text:
                        skills = li.find("strong").text.strip() if li.find("strong") else li.text.strip()

                date_tag = offer.find("time")
                publication_date = date_tag.text.strip() if date_tag else "N/A"

                job_listings.append({
                    "Titre": title,
                    "Entreprise": company,
                    "Localisation": location,
                    "Compétences clés": skills,
                    "Date de publication": publication_date,
                    "Lien": link
                })
            time.sleep(2)
             # to-csv 
           
            with open('job_listings.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=job_listings[0].keys())
                writer.writeheader()
                writer.writerows(job_listings)
        return job_listings
