from flask import render_template
from app import app

from app.models import latest_blocks as latest_blocks_model
from app.views import latest_blocks as latest_blocks_view

from app.models import block as block_model
from app.views import block as block_view

@app.route('/')
@app.route('/index')
def index():
    # Get the latest blocks
    blocks = latest_blocks_model.get_latest_blocks(6)
    blocks = latest_blocks_view.get_latest_blocks(blocks)
    return render_template ('index.html', blocks=blocks)

@app.route ('/block/<int:height>')
def block (height):
    block = block_model.get_block (height)
    block = block_view.get_block (block)

    if height != 0:
        previous_block = block_model.get_block (height-1)
        previous_block = block_view.get_block (previous_block)
    else:
        previous_block = None

    return render_template ('block.html', block=block, previous_block=previous_block)
