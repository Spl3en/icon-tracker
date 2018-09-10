from app.models.icon import icon_service

def get_address (hash):
    return {
        'hash' : hash, 
        'balance' : icon_service.get_balance (hash)
    }