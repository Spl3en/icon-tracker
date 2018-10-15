
def get_transactions (transactions):
    for tx in transactions:
        tx['amount_icx'] = float(int(tx['value']) / 10**18)
        
    return transactions