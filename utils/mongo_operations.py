import pymongo
import hashlib

class MongoDBOperations:
    def __init__(self, uri):
        self.client = pymongo.MongoClient(uri,socketTimeoutMS=30000, 
                             connectTimeoutMS=30000)
        self.db = self.client["med_ai_database"]
        self.collection = self.db["users"]

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def signup(self, name, email, password):
        hashed_password = self.hash_password(password)
        if self.collection.find_one({"email": email}):
            return False
        self.collection.insert_one({"name": name, "email": email, "password": hashed_password})
        return True

    def login(self, email, password):
        hashed_password = self.hash_password(password)
        user = self.collection.find_one({"email": email, "password": hashed_password})
        return user is not None

    def close_connection(self):
        self.client.close()
