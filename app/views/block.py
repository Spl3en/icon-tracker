import time

def get_block (block):
    block['timestamp'] = time.strftime ('%Y-%m-%d %H:%M:%S', time.gmtime (block['time_stamp'] / (1000 * 1000)))
    block['hash'] = block['block_hash']

    amount_loop = 0

    for tx in block['confirmed_transaction_list']:

        # Transaction values transfered
        if 'value' in tx:
            if 'from' in tx:
                amount_loop += int (tx['value'], 16)

        # Account creation value
        if 'accounts' in tx:
            for account in tx['accounts']:
                amount_loop += int(account['balance'], 16)

    block['amount_loop'] = amount_loop
    block['amount_icx'] = float(amount_loop / (10 ** 18))

    return block