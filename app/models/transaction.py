from app.models.icon import icon_service
import copy

def get_transactions (block):

    txs = []
    
    # Get information about each tx in order to retrieve the tx fee

    for tx in block['confirmed_transaction_list']:

        # Transaction values transfered
        if 'value' in tx:
            tx['value'] = int(tx['value'], 16)
        else:
            tx['value'] = 0

        # Account creation value
        if 'accounts' in tx:
            for account in tx['accounts']:
                tx = copy.deepcopy(tx)
                print(tx)
                print(account)
                tx['from'] = None
                tx['to'] = account['address']
                tx['txHash'] = account['name']
                tx['value'] = int(account['balance'], 16)
                txs.append(tx)
        else:
            txs.append(tx)

        # XXX: Where is the tx fee field in v3 ?
        # XXX: https://www.icondev.io/community/forum/forumDetail.do?bbs_No=15

    return txs