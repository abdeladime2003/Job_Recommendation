from Scraper.ScraperSrc import *
from Scraper.Sender import *
from config import *
#Initialisation

sender = Sender()
Instance = AnapecScraper(driver_path=driverPath, sender=sender,endpoint=endpoint)


###Scraping
Instance.scrape_job_offers(Site)

DataFrame = Instance.get_output_dataframe()

DataFrame.to_csv(csvPath)