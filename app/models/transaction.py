from app.models.icon import get_icon_service
import copy

def get_transactions (session, block):

    icon_service = get_icon_service (session)

    txs = []
    
    # Get information about each tx in order to retrieve the tx fee

    for tx in block['confirmed_transaction_list']:

        # Transaction values transfered
        if 'value' in tx:
            tx['value'] = tx['value']
        else:
            tx['value'] = 0

        # Account creation value
        if 'accounts' in tx:
            for account in tx['accounts']:
                tx = copy.deepcopy(tx)
                tx['from'] = None
                tx['to'] = account['address']
                tx['txHash'] = account['name']
                try:
                    tx['value'] = int(account['balance'], 16)
                except:
                    tx['value'] = 0
                txs.append(tx)
        else:
            txs.append(tx)

        # XXX: Where is the tx fee field in v3 ?
        # XXX: https://www.icondev.io/community/forum/forumDetail.do?bbs_No=15

    return txs