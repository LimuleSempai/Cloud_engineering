from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client.receipts_db
collection = db.receipts

@app.get("/receipts/{shop_name}")
async def get_receipts(shop_name: str):
    receipts = collection.find({'shop_name': shop_name})
    return list(receipts)
