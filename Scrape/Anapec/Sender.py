import requests

class Sender:
    @staticmethod
    def sendData(data, endpoint):
        requests.post(endpoint, json = data)