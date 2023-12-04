# ticket_generator_test.py
from ticket_generator import generate_ticket

def test_ticket_generator():
    ticket = generate_ticket()
    assert 'shop_name' in ticket
    assert 'checkout_id' in ticket
    assert 'cashier_id' in ticket
    assert 'products' in ticket
    assert isinstance(ticket['products'], list)
