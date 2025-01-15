# main.py

import logging
from scraper.scraper import Scraper
from scraper.sender import Sender

def main():
    logging.info("Démarrage du scraping...")
    
    scraper = Scraper()
    sender = Sender()

    try:
        job_data = scraper.scrape(max_pages=2)
        sender.send(job_data)
    except Exception as e:
        logging.error(f"Erreur durant l'exécution : {e}")

    logging.info("Fin du processus.")

if __name__ == "__main__":
    main()
