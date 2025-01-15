import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# En-têtes pour simuler un navigateur
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# URL de base avec pagination
base_url = "https://www.rekrute.com/offres.html?s=1&p={}&o=1"

def scrape_rekrute(pages=5):
    job_listings = []

    # Parcourir les 5 premières pages
    for page in range(1, pages + 1):
        url = base_url.format(page)
        print(f" Scraping page {page}: {url}")

        # Requête HTTP
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Erreur lors de l'accès à {url}: {e}")
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        offers = soup.find_all("li", class_="post-id")

        if not offers:
            print(f" Aucune offre trouvée sur la page {page}.")
            continue

        for offer in offers:
            # Titre du poste
            title_tag = offer.find("h2")
            title = title_tag.text.strip() if title_tag else "N/A"

            # Entreprise dans sopan de style = style="color: #5b5b5b;" premier elemnt d indice 0
            img_tag = offer.find("img", class_="photo")
            company = img_tag['title'].strip() if img_tag and img_tag.has_attr('title') else "N/A"

            # Description
            description_tag = offer.find("div", class_="info")
            description = description_tag.text.strip() if description_tag else "N/A"

            # Date de publication
            date_tag = offer.find("em", class_="date")
            publication_date = date_tag.text.strip() if date_tag else "N/A"

            # Secteur d'activité
            sector_tag = offer.find("a", href=lambda x: x and "sectorId" in x)
            sector = sector_tag.text.strip() if sector_tag else "N/A"

            # Fonction
            function_tag = offer.find("a", href=lambda x: x and "positionId" in x)
            function = function_tag.text.strip() if function_tag else "N/A"

            # Expérience requise
            experience_tag = offer.find("a", href=lambda x: x and "workExperienceId" in x)
            experience = experience_tag.text.strip() if experience_tag else "N/A"

            # Niveau d'étude demandé
            study_tag = offer.find("a", href=lambda x: x and "studyLevelId" in x)
            study_level = study_tag.text.strip() if study_tag else "N/A"

            # Type de contrat
            contract_tag = offer.find("a", href=lambda x: x and "contractType" in x)
            contract_type = contract_tag.text.strip() if contract_tag else "N/A"

            # Stocker les données
            job_listings.append({
                "Titre": title,
                "Entreprise": company,
                "Description": description,
                "Date de publication": publication_date,
                "Secteur d'activité": sector,
                "Fonction": function,
                "Expérience requise": experience,
                "Niveau d'étude": study_level,
                "Type de contrat": contract_type
            })

        # Pause entre les pages pour éviter le blocage
        time.sleep(2)

    # Convertir en DataFrame
    df = pd.DataFrame(job_listings)
    if not df.empty:
        df.to_csv("offres_rekrute.csv", index=False, encoding='utf-8-sig')
        print(" Scraping terminé ! Données sauvegardées dans **offres_rekrute.csv**.")
    else:
        print(" Aucune donnée collectée.")

# Exécution du scraping sur 5 pages
scrape_rekrute(pages=5)
