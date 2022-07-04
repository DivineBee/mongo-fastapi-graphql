from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
password = os.environ.get("MONGO_PASSWORD")
conn = MongoClient(f"mongodb+srv://user:{password}@clusterfastapi.pypfeid.mongodb.net/?retryWrites=true&w=majority")
db = conn['cars']