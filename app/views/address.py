
def get_address (address):
    address['balance'] = address['balance'] / 10**18
    return address