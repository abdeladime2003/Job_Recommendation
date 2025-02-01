import requests
from bs4 import BeautifulSoup
import time
import csv
import logging
from config import BASE_URL, HEADERS, CSV_FILE_PATH
from datetime import datetime , timedelta
## -10 days
date_today = (datetime.today() - timedelta(days=10) ).strftime('%d.%m.%Y')
class Scraper:  
    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Gecko/20100101 Firefox/89.0'
        }
    def scrape(self, max_pages=20):
        job_listings = []
        logging.info("Début du scraping des offres d'emploi.")

        for page in range(0, max_pages + 1):
            url = f"{self.base_url}?page={page}"
            logging.info(f"Scraping de la page : {url}")

            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
            except requests.RequestException as e:
                logging.error(f"Erreur lors de l'accès à {url} : {e}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            offers = soup.find_all("div", class_="card-job-detail")

            if not offers:
                logging.warning(f"Aucune offre trouvée sur la page {page}.")
                continue

            # Initialize variables before the loop
            Niveau_Etudes, Niveau_Exp, Contrat, skills = "N/A", "N/A", "N/A", "N/A"

            for offer in offers:
                title_tag = offer.find("h3").find("a")
                title = title_tag.text.strip() if title_tag else "N/A"
                description = offer.find("p", class_="card-job-description").text.strip() if offer.find("p", class_="card-job-description") else "N/A"
                link = f"https://www.emploi.ma{title_tag.get('href')}" if title_tag else "N/A"
                company = offer.find("a", class_="card-job-company company-name").text.strip() if offer.find("a", class_="card-job-company company-name") else "N/A"

                # Extract location
                location = next((li.find("strong").text.strip() for li in offer.find_all("li") if "Région de" in li.text), "N/A")

                # Loop through li to get other details
                for li in offer.find_all("li"):
                    if "Niveau d´études requis" in li.text:
                        Niveau_Etudes = li.find("strong").text.strip() if li.find("strong") else li.text.strip()
                    elif "Niveau d'expérience" in li.text:
                        Niveau_Exp = li.find("strong").text.strip() if li.find("strong") else li.text.strip()
                    elif "Contrat proposé" in li.text:
                        Contrat = li.find("strong").text.strip() if li.find("strong") else li.text.strip()
                    elif "Compétences clés" in li.text:
                        skills = li.find("strong").text.strip() if li.find("strong") else li.text.strip()

                # Extract publication date
                date_tag = offer.find("time")
                date = date_tag.text.strip() if date_tag else "N/A"
                ## compare date
                if date >= date_today:
                    publication_date = date
                else:
                    continue

                # Append job details to the list
                job_listings.append({
                    "titre": title,
                    "entreprise": company,
                    "localisation": location,
                    "competences_cles": skills.split("-") if skills != "N/A" else [],
                    "niveau_etudes_requis": Niveau_Etudes,
                    "niveau_experience": Niveau_Exp,
                    "contrat_propose": Contrat,
                    "date_publication": publication_date,
                    "lien": link
                })

            logging.info(f"{len(offers)} offres extraites de la page {page}.")
            time.sleep(2)

        self.save_to_csv(job_listings)
        logging.info(f"Scraping terminé. Total des offres récupérées : {len(job_listings)}.")
        return job_listings

    def save_to_csv(self, data):
        try:
            with open(CSV_FILE_PATH, 'a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            logging.info(f"Données sauvegardées dans {CSV_FILE_PATH}")
        except Exception as e:
            logging.error(f"Erreur lors de la sauvegarde des données dans le CSV : {e}")
