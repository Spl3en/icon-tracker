
def get_transactions (transactions):
    for tx in transactions:
        print(tx['value'])
        tx['amount_icx'] = float(int(tx['value']) / 10**18)
        
    return transactions