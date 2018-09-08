import time

def get_block (block):
    block['timestamp'] = time.strftime ('%Y-%m-%d %H:%M:%S', time.gmtime (block['time_stamp'] / (1000 * 1000)))
    block['hash'] = block['block_hash']

    amount_icx = 0
    for tx in block['confirmed_transaction_list']:
        if "value" in tx:
            if "from" in tx:
                amount_icx += int(tx['value'], 16)
            if "to" in tx:
                amount_icx += int(tx['value'], 16)

    block['amount_icx'] = amount_icx
    block['amount_icx_hex'] = hex(amount_icx)

    return block