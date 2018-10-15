from app.models.icon import get_icon_service

def get_latest_blocks (session, count):

    icon_service = get_icon_service (session)

    blocks = []
    last = 0

    for i in range (count):
        if i == 0:
            block = icon_service.get_block ('latest')
            last = block['height']
        else:
            last -= 1
            block = icon_service.get_block (last)

        blocks.append (block)

    return blocks