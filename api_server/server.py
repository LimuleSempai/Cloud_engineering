from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from kafka import KafkaProducer

app = FastAPI()

class Receipt(BaseModel):
    shop_name: str
    checkout_id: int
    cashier_id: int
    products: list
    total_price: float

#producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer = KafkaProducer(bootstrap_servers=['kafka:9092'], value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.post("/receipts")
async def receive_receipt(receipt: Receipt):
    try:
        producer.send('receipts_topic', receipt.dict())
        return {"message": "Receipt sent to Kafka"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
