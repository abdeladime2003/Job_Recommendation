from pymongo import MongoClient, errors

def get_mongo_connection():
    try:
        # Connexion au serveur MongoDB
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
        
        # Vérification de la connexion au serveur
        client.server_info()  # Déclenche une exception si le serveur est injoignable
        
        # Nom de la base de données et de la collection
        db_name = 'job_recommendation'
        collection_name = 'cvs'

        # Vérification de l'existence de la base de données
        if db_name not in client.list_database_names():
            print(f" La base de données '{db_name}' n'existe pas.")
            return None

        db = client[db_name]

        # Vérification de l'existence de la collection
        if collection_name not in db.list_collection_names():
            print(f" La collection '{collection_name}' n'existe pas dans la base de données '{db_name}'.")
            return None

        # Retourne la collection si tout est en ordre
        Cvs = db[collection_name]
        print(" Connexion à la collection MongoDB établie.")
        return Cvs

    except errors.ServerSelectionTimeoutError:
        print(" Le serveur MongoDB est injoignable.")
        return None

    except Exception as e:
        print(" Une erreur est survenue :", e)
        return None

# Appel de la fonction
get_mongo_connection()
