import time

def get_block (block):
    block['timestamp'] = time.strftime ('%Y-%m-%d %H:%M:%S', time.gmtime (block['time_stamp'] / (1000 * 1000)))
    block['hash'] = block['block_hash']

    amount_icx = 0

    for tx in block['confirmed_transaction_list']:

        # Transaction values transfered
        if 'value' in tx:
            if 'from' in tx:
                amount_icx += int(tx['value'], 16)
            if 'to' in tx:
                amount_icx += int(tx['value'], 16)

        # Account creation value
        if 'accounts' in tx:
            for account in tx['accounts']:
                amount_icx += int(account['balance'], 16)

    block['amount_icx'] = amount_icx

    return block