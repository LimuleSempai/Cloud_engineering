from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient('localhost', 27017)
db = client.receipts_db
collection = db.receipts

# Set up Kafka consumer
consumer = KafkaConsumer(
    'receipts_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    # Save message to MongoDB
    collection.insert_one(message.value)
    print(f"Saved receipt to MongoDB: {message.value}")
