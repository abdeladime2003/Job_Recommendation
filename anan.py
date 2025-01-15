from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import geckodriver_autoinstaller
# Configurer Selenium pour un navigateur sans interface graphique (headless)
options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Lancer le navigateur
geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
driver.get("https://joblik.ma/jobs")
time.sleep(2)
# Cliquer plusieurs fois sur "Voir Plus" pour charger toutes les offres
while True:
    try:
        voir_plus_button = driver.find_element(By.XPATH, '//button[contains(text(), "Voir Plus")]')
        voir_plus_button.click()
        time.sleep(2)  # Laisse le temps au contenu de se charger
    except:
        print("Plus de bouton 'Voir Plus' trouvé.")
        break

# Extraire les offres après avoir chargé toute la page
jobs = driver.find_elements(By.CLASS_NAME, "job-card")
job_listings = []

for job in jobs:
    try:
        title = job.find_element(By.CLASS_NAME, "job-title").text
    except:
        title = "N/A"

    try:
        company = job.find_element(By.CLASS_NAME, "job-company").text
    except:
        company = "N/A"

    try:
        location = job.find_element(By.CLASS_NAME, "fa-map-marker-alt").find_element(By.XPATH, "..").text
    except:
        location = "N/A"

    try:
        description = job.find_element(By.CLASS_NAME, "job-description").text
    except:
        description = "N/A"

    try:
        deadline = job.find_element(By.XPATH, './/strong[contains(text(),"Date limite")]/following-sibling::text()').strip()
    except:
        deadline = "N/A"

    job_listings.append({
        "Titre": title,
        "Entreprise": company,
        "Localisation": location,
        "Description": description,
        "Date limite": deadline
    })

# Fermer le navigateur
driver.quit()

# Sauvegarder les données dans un CSV
df = pd.DataFrame(job_listings)
df.to_csv("offres_joblik.csv", index=False, encoding="utf-8-sig")

print("Scraping terminé ! Données sauvegardées dans offres_joblik.csv.")
