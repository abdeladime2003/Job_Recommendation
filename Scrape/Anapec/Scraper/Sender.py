import requests
import logging
import Scrape.Anapec.config
class Sender:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    
    def sendData(self,endpoint,data, attempt = 3):
        for i in range(attempt):
            try:
            
                req = requests.post(endpoint, json = data)
                print(req.status_code)
                if req.status_code == 201:
                    self.logger.info(f"Connection Established!")
                    break
                else : 
                    self.logger.error(f"attempt {i} Failed to connect, code status {req.status_code}")
                    continue
            except Exception as e:
                self.logger.critical("Couldn't find the api endpoint")