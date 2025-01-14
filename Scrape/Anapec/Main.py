from Scraper import *

driverPath = "driver/geckodriver.exe"
endpoint = "https://719d-105-155-133-97.ngrok-free.app/api/add-job-offer/"
Instance = AnapecScraper(driver_path=driverPath, endpoint=endpoint)
Site = 'https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg=1'

Instance.scrape_job_offers(Site)

#DataFrame = Instance.get_output_dataframe()

#DataFrame.to_csv("Prod.csv")