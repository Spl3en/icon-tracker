from app.models.icon import get_icon_service

def get_block (session, height):

    icon_service = get_icon_service (session)

    return icon_service.get_block (height)
