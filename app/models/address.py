from app.models.icon import get_icon_service

def get_address (session, hash):
    
    icon_service = get_icon_service (session)

    return {
        'hash' : hash, 
        'balance' : icon_service.get_balance (hash)
    }