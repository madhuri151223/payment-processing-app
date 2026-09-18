from app import process_payment

def test_payment():
    assert process_payment(1000, 5) == 1050
