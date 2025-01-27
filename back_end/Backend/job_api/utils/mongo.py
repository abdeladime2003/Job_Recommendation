from pymongo import MongoClient, errors

def get_mongo_connection():
    try:
        client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
        db = client['job_recommendation']
        job_offers_collection = db['job_offers']
        return job_offers_collection

    except errors.ServerSelectionTimeoutError:
        print("❌ Le serveur MongoDB est injoignable.")
        return None

    except Exception as e:
        print("❌ Une erreur est survenue :", e)
        return None
