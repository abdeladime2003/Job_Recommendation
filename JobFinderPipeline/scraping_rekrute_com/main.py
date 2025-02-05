import logging
from scraper.scraping import RekruteScraper
from scraper.sender import Sender
from config import CSV_FILE_PATH
import sys
def main():
    logging.info("Démarrage du processus de scraping et d'envoi des données...")

    # Étape 1 : Scraper les données
    scraper = RekruteScraper(total_pages=3)  
    try:
        scraper.scrape_all_pages()
        scraper.save_to_csv()
    except Exception as e:
        logging.error(f"Erreur lors du scraping : {e}")
        sys.exit(1)
    finally:
        scraper.close_driver()
    sender = Sender()
    try:
        sender.send(scraper.data)
    except Exception as e:
        logging.error(f" Erreur lors de l'envoi des données : {e}")
        sys.exit(1)
    finally:
        sender.close_session()

    logging.info(" Processus terminé avec succès.")
    sys.exit(0)
if __name__ == "__main__":
    main()
