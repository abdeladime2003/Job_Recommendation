from typing import Dict, Optional
import logging

from pymongo import MongoClient


class MongoDbStorage:
    """
    A class for storing Python dictionaries in MongoDB.
    
    This class manages connections to MongoDB and provides methods
    for storing and retrieving dictionary data.
    """
    def __init__(self, db_name: str, collection_name: str, connetion_string: str ="mongodb://localhost:27017/"):
        """
        Initialize the DictionaryStorage with MongoDB connection details.
        
        Args:
            db_name (str): Name of the MongoDB database
            collection_name (str): Name of the collection to store data
            connection_string (str): MongoDB connection URI (defaults to localhost)
        """
        self.logger = logging.getLogger(__name__)
        self.connection_string = connetion_string
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = None
        self.db = None
        self.collection = None


    def connect(self) -> bool:
        """
        Establish connection to MongoDB.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]

            self.client.server_info()   # Test connection
            self.logger.info(f"Successfully connected to MongoDB: {self.db_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to connect to MongoDB: {e}")
            return False
    

    def store_dictionary(self, data: Dict) -> Optional[str]:
        """
        Store a dictionary in MongoDB.
        
        Args:
            data (Dict): The dictionary to store
            
        Returns:
            Optional[str]: The ObjectId of inserted document as string if successful, None otherwise
        """
        if not self.client:
            if not self.connect():
                return None
        
        try:
            result = self.collection.insert_one(data)
            self.logger.info(f"Successfully stored dictionary with ID: {result.inserted_id}")
            return str(result.inserted_id)
        except Exception as e:
            self.logger.error(f"Failed to store dictionary: {e}")
            return None
        
    
    def close(self):
        if self.client:
            self.client.close()
            self.client = None
            self.logger.info("MongoDB connection closed")