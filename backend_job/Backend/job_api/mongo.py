from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Access the database
db = client['job_recommendation']

# Access the job_offers collection
job_offers_collection = db['job_offers']
