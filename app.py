def process_payment(amount, fee_percentage):
    fee = amount * fee_percentage / 100
    return amount + fee
  
