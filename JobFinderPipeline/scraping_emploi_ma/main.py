import logging
from scraper.scraper import Scraper
from scraper.sender import Sender
import sys
def main():
    logging.info("Démarrage du scraping...")
    
    scraper = Scraper()
    sender = Sender()

    try:
        job_data = scraper.scrape()
        sender.send(job_data)
    except Exception as e:
        logging.error(f"Erreur durant l'exécution : {e}")
        sys.exit(1)
    logging.info("Fin du processus.")
    sys.exit(0)

if __name__ == "__main__":
    main()
