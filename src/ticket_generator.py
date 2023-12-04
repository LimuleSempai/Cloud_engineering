import requests
import json
from faker import Faker

fake = Faker()

def generate_ticket():
    return {
        'shop_name': fake.company(),
        'checkout_id': fake.random_int(min=1, max=100),
        'cashier_id': fake.random_int(min=1, max=10),
        'products': [
            {
                'name': fake.word(),
                'price': fake.random_number(digits=2),
                'quantity': fake.random_int(min=1, max=10),
            }
            for _ in range(fake.random_int(min=1, max=5))
        ],
        'total_price': fake.random_number(digits=2),
    }

def send_ticket_to_server(ticket):
    url = 'http://localhost:8000/receipts'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(ticket))
    return response

if __name__ == "__main__":
    ticket = generate_ticket()
    response = send_ticket_to_server(ticket)
    print("Ticket sent, server responded with status code:", response.status_code)
