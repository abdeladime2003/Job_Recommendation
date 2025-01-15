from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import Sender
import pandas as pd
import requests
import json


class AnapecScraper:
    """"Cette Class represente Un script de scraping du site marocain Anapec"""
    """Ce Script est Concu pour prelever le Lien de l'offre, Description, Competence cherche, Type de contrat"""
    def __init__(self, driver_path, endpoint, sender):
        self.driver_path = driver_path
        self.service = Service(self.driver_path)
        self.driver = webdriver.Firefox(service=self.service)
        self.output_dataframe = pd.DataFrame(columns=["Description", "Lien", "Contrat", "Lieu", "comptence"])
        self.anapec = "https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg="
        self.endpoint = endpoint 
        self.sender = sender
    def open_website(self, url, attempts=3, wait=10):
        for attempt in range(attempts):
            try: 
                self.driver.get(url)    
                if self.driver.current_url == url:
                    break
            except WebDriverException as e:
                print(f"{attempt} failed retrying in {wait} seconds")

    def get_offres_pages(self, url):
        self.open_website(url)
        pages = self.driver.find_elements(By.XPATH, "//nav[@aria-label=' Page navigation ']//ul//li//a")
        return int(pages[-1].text)

    def scrape_job_offers(self, page_offres):
        offres_pages = self.get_offres_pages(page_offres)
        for i in range(1, offres_pages + 1):
            page = self.anapec + str(i)
            self.open_website(page)
            job_offers = self.driver.find_elements(By.CSS_SELECTOR, "div.offres-item")
            for job_offer in job_offers:
                data = {}
                job_offer.click()
                tab = self.driver.window_handles
                self.driver.switch_to.window(tab[-1])
                try:
                    info_offre = WebDriverWait(self.driver, 20).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.small_puce + span"))
                    )
                except TimeoutException:
                    self.driver.close()
                    self.driver.switch_to.window(tab[0])
                    continue
                titre_champs = self.driver.find_elements(By.CSS_SELECTOR, "span.small_puce")
                desc = self.driver.find_element(By.CSS_SELECTOR, "span.ref_offre2")
                data['Description'] = desc.text
                data['comptence'] = []
                try:
                    comptences = self.driver.find_elements(By.XPATH, "//ul[@class='liste-affiche-offre']//li")
                    for competence in comptences:
                        data['comptence'].append(competence.text)
                        if isinstance(data['comptence'], str):
                            try:
                                data['comptence'] = json.loads(data['comptence']) 
                            except json.JSONDecodeError:
                                data['comptence'] = [] 


                except NoSuchElementException:
                    pass
                data["Lien"] = self.driver.current_url
                for titre_champ, info in zip(titre_champs, info_offre):
                    if titre_champ.text == 'Type de contrat :':
                        data["Contrat"] = info.text
                    if titre_champ.text == 'Lieu de travail :':
                        data["Lieu"] = info.text
                data['Date'] = info_offre[-1].text
                
                self.sender.sendData(data = data,endpoint = self.endpoint)
                requests.post(self.endpoint, data=data)
              #  self.output_dataframe = pd.concat( ignore_index=True)
                self.driver.close()
                self.driver.switch_to.window(tab[0])
                
                
        self.driver.quit()

    def get_output_dataframe(self):
        return self.output_dataframe


# Usage example:
# scraper = AnapecScraper('driver/geckodriver.exe', 'http://example.com/endpoint')
# scraper.scrape_job_offers('https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg=1')
# df = scraper.get_output_dataframe()
# df.to_csv("Prod.csv")
