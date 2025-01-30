from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import numpy as np
import re
##from config import BASE_URL, HEADERS, CSV_FILE_PATH

class RekruteScraper:
    def __init__(self, base_url='https://www.rekrute.com/offres.html?s=1&p={}&o=1', total_pages=1):
        self.base_url = base_url
        self.total_pages = total_pages
        self.data = []
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def scrape_page(self, page):
        print(f"Scraping de la page {page}/{self.total_pages}...")
        self.driver.get(self.base_url.format(page))
        time.sleep(3)

        offres = self.driver.find_elements(By.CLASS_NAME, 'post-id')

        for offre in offres:
            try:
                description_poste = offre.find_element(By.XPATH, ".//i[@class='fa fa-binoculars']/following-sibling::span").text
            except:
                description_poste = np.nan

            try:
                titre_localisation = offre.find_element(By.TAG_NAME, 'h2').text
                titre, localisation = titre_localisation.split(' | ')
            except:
                titre = np.nan
                localisation = np.nan

            try:
                lien = offre.find_element(By.CLASS_NAME, 'titreJob').get_attribute('href')
            except:
                lien = np.nan

            try:
                entreprise = offre.find_element(By.TAG_NAME, 'img').get_attribute('title')
            except:
                entreprise = np.nan

            try:
                date_postes = offre.find_element(By.CLASS_NAME, 'date').text
                date, nombre_postes = date_postes.split(' | ')
            except:
                date = np.nan
                nombre_postes = np.nan

            experience, niveau_etude, type_contrat, teletravail, competences = (np.nan, np.nan, np.nan, np.nan, np.nan)

            try:
                info = offre.find_element(By.TAG_NAME, 'ul')
                for li in info.find_elements(By.TAG_NAME, 'li'):
                    if 'Expérience requise' in li.text:
                        experience = li.find_element(By.TAG_NAME, 'a').text
                    elif "Niveau d'étude demandé" in li.text:
                        niveau_etude = li.find_element(By.TAG_NAME, 'a').text
                    elif "Type de contrat proposé" in li.text:
                        type_contrat = li.find_element(By.TAG_NAME, 'a').text
                        if 'Télétravail' in li.text:
                            teletravail = 'Oui' if 'Oui' in li.text else 'Non'
                    elif "Fonction" in li.text:
                        competences = li.find_element(By.TAG_NAME, 'a').text.split("/")
            except:
                pass
            try : # Publication : du 16/01/2025 au 16/03/2025 
                date_publication = re.search(r"du (\d{2}/\d{2}/\d{4}) au (\d{2}/\d{2}/\d{4})", date).group(1).strip().replace('/','.')
                date_limite = re.search(r"du (\d{2}/\d{2}/\d{4}) au (\d{2}/\d{2}/\d{4})", date).group(2).strip().replace('/','.')
            except:
                date_publication = np.nan
                date_limite = np.nan
            self.data.append({
                'titre': titre,
                'entreprise': entreprise,
                'description': description_poste,
                'localisation': localisation,
                'date_publication': date_publication,
                'date_limite': date_limite,
                'nombre_postes': nombre_postes,
                'niveau_experience': experience,
                'niveau_etudes_requis': niveau_etude,
                'competences_cles': competences,
                'contrat_propose': type_contrat,
                'teletravail': teletravail,
                'lien': lien,
            })

    def scrape_all_pages(self):
        for page in range(1, self.total_pages + 1):
            self.scrape_page(page)

    def save_to_csv(self, filename=r'C:\Users\LENOVO\Desktop\project_job\JobFinderPipeline\data\offres_rekrute.csv'):
        ## ajouter au data exisitant 
        try:
            df = pd.read_csv(filename)
            df = pd.concat([df, pd.DataFrame(self.data)])
        except:
            df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Données enregistrées dans {filename}.")
        

    def close_driver(self):
        self.driver.quit()
