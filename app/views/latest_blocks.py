from app.views.block import get_block

def get_latest_blocks (blocks):
    blocks = map (get_block, blocks)
    return blocks