# Database Setup
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["users_data"]
user_collection = db["users"]
