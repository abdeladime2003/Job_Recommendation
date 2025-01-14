from anapecUtilities import *

driverPath = "driver/geckodriver.exe"

Instance = AnapecScraper(driver_path=driverPath)
Site = 'https://anapec.ma/home-page-o1/chercheur-emploi/offres-demploi/?pg=1'

Instance.scrape_job_offers(Site)

DataFrame = Instance.get_output_dataframe()

DataFrame.to_csv("Prod.csv")