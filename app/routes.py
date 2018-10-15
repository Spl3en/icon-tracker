from flask import render_template, session, request, redirect, url_for
from app import app, constants
from app.models import latest_blocks as latest_blocks_model
from app.views import latest_blocks as latest_blocks_view
from app.models import block as block_model
from app.views import block as block_view
from app.models import transaction as transaction_model
from app.views import transaction as transaction_view
from app.models import address as address_model
from app.views import address as address_view

@app.route('/')
@app.route('/index')
def index():
    # Get the latest blocks
    blocks = latest_blocks_model.get_latest_blocks (session, 6)
    blocks = latest_blocks_view.get_latest_blocks (blocks)

    #Get genesis block
    genesis = block_model.get_block (session, 0)
    genesis = block_view.get_block (genesis)

    return render_template ('index.html', session=session, constants=constants, blocks=blocks, genesis=genesis)

@app.route ('/set_nid/<int:nid>')
def set_nid (nid):
    session["nid"] = nid
    
    if (session["nid"] < 0 or session["nid"] > len(constants.NETWORK_ENDPOINTS)):
        session["nid"] = 0

    return redirect (url_for('index'))

@app.route ('/block/<int:height>')
def block (height):

    block = block_model.get_block (session, height)
    block = block_view.get_block (block)

    if height != 0:
        previous_block = block_model.get_block (session, height-1)
        previous_block = block_view.get_block (previous_block)
    else:
        previous_block = None

    return render_template ('block.html', session=session, constants=constants, block=block, previous_block=previous_block)


@app.route ('/blocktx/<int:height>')
def blocktx (height):

    block = block_model.get_block (session, height)
    block = block_view.get_block (block)

    transactions = transaction_model.get_transactions (session, block)
    transactions = transaction_view.get_transactions (transactions)
    
    return render_template ('blocktx.html', session=session, constants=constants, block=block, transactions=transactions)


@app.route ('/address/<string:address>')
def address (address):

    address = address_model.get_address (session, address)
    address = address_view.get_address (address)

    return render_template ('address.html', session=session, constants=constants, address=address)
