from app.models.icon import icon_service

def get_latest_blocks (count):

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