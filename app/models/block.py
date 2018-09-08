from app.models.icon import icon_service

def get_block (height):
    return icon_service.get_block (height)
