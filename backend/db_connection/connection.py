from pymongo import MongoClient
from config import MONGO_URI,DATABASE_NAME
client = MongoClient(MONGO_URI)  # Change the URI if using a cloud database
db = client.joke_chatgpt_db
user_collection = db.users_data
jokes_collection = db.jokes_data

