from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import re
from datetime import datetime
import logging
import config
import pandas as pd
import json


class AnapecScraper:
    """"Cette Class represente Un script de scraping du site marocain Anapec"""
    """Ce Script est Concu pour prelever le Lien de l'offre, Description, Competence cherche, Type de contrat"""
    def __init__(self, driver_path, sender, endpoint):
        self.driver_path = driver_path
        self.service = Service(self.driver_path)
        self.driver = webdriver.Firefox(service=self.service)
        self.output_dataframe = pd.DataFrame(columns=["description", "lien", "contrat_propose", "localisation", "competences_cles"])
        self.anapec = "https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg="
        self.sender = sender
        self.endpoint = endpoint
        self.logger = logging.getLogger(__name__)

    def open_website(self, url, attempts=3, wait=10):
        for attempt in range(attempts):
            try: 
                self.driver.get(url)    
                if self.driver.current_url == url:
                    self.logger.info("Connected to Server successfully")
                    break
            except WebDriverException as e:
                self.logger.warning(f"{attempt} failed retrying in {wait} seconds")



    def get_offres_pages(self, url):
        self.open_website(url)
        self.logger.info("Page opened Succefully")
        pages = self.driver.find_elements(By.XPATH, "//nav[@aria-label=' Page navigation ']//ul//li//a")
        return int(pages[-1].text)



    def scrape_job_offers(self, page_offres):
        offres_pages = self.get_offres_pages(page_offres)
        self.logger.info("Started Scraping")
        
        # Increase range for more pages
        for i in range(1, 3):
            self.logger.info(f"Scraping page {i}")
            page = self.anapec + str(i)
            self.open_website(page)
            job_offers = self.driver.find_elements(By.CSS_SELECTOR, "div.offres-item")
            
            # Process each job offer on the page
            for job_offer in job_offers:
                try:
                    data = {}
                    job_offer.click()
                    tab = self.driver.window_handles
                    self.driver.switch_to.window(tab[-1])
                    
                    # Get offer details
                    try:
                        info_offre = WebDriverWait(self.driver, 20).until(
                            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.small_puce + span"))
                        )
                        titre_champs = self.driver.find_elements(By.CSS_SELECTOR, "span.small_puce")
                        desc = self.driver.find_element(By.CSS_SELECTOR, "span.ref_offre2")
                        data['description'] = desc.text
                        data['competences_cles'] = []
                        try:
                            comptences = self.driver.find_elements(By.XPATH, "//ul[@class='liste-affiche-offre']//li")
                            for competence in comptences:
                                data['competences_cles'].append(competence.text)
                                if isinstance(data['competences_cles'], str):
                                    try:
                                        data['competences_cles'] = json.loads(data['competences_cles']) 
                                        self.logger.debug("Transforming the str list into a list")
                                    except json.JSONDecodeError:
                                        data['competences_cles'] = [] 
                        except NoSuchElementException:
                            self.logger.error(f"No competence listed for f{data['description']}")
                        data["lien"] = self.driver.current_url
                        for titre_champ, info in zip(titre_champs, info_offre):
                            if titre_champ.text == 'Type de contrat :':
                                data["contrat_propose"] = info.text
                            if titre_champ.text == 'Lieu de travail :':
                                data["localisation"] = info.text
                            if titre_champ.text == 'Date de début  : ':
                                date_pattern = r'\b\d{2}:\d{2}:\d{4}\b'
                                match = re.search(date_pattern, info.text)
                                if match:
                                # Parse and return the datetime object if found
                                    data['date'] =  datetime.strptime(match.group(), '%d:%m:%Y').date()
                                else :
                                    data['date'] = None
                        
                        # Store data
                        self.logger.info("Sending Data into Database")
                        self.sender.sendData(endpoint = self.endpoint, data = data)
                        self.output_dataframe = pd.concat([self.output_dataframe, pd.DataFrame([data])], ignore_index=True)
                        
                    except TimeoutException:
                        self.logger.error(f"Timeout on page {i}, offer skipped")
                        
                    finally:
                        # Always close the tab and switch back
                        self.driver.close()
                        self.driver.switch_to.window(tab[0])
                        
                except Exception as e:
                    self.logger.error(f"Error processing offer on page {i}: {str(e)}")
                    continue
                    
            self.logger.info(f"Completed page {i}")
            
        self.driver.quit()
        self.logger.info("Scraping completed")



    def get_output_dataframe(self):
        return self.output_dataframe


