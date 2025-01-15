from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    client.server_info()  # Teste la connexion
    print("Connexion réussie à MongoDB.")
except ConnectionFailure as e:
    print(f"Échec de la connexion à MongoDB : {e}")
