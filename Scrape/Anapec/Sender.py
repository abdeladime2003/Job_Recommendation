import requests

class Sender:
    @staticmethod
    def sendData(data, endpoint, attempt = 3):
        for i in range(attempt):
            try:
            
                req = requests.post(endpoint, json = data)
                if req.status_code == 200:
                    break
                else : continue
            except Exception as e:
                pass