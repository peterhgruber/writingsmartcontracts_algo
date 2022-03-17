""" Utility functions and shortcuts for the WSC winter school
    (c) 2022 peter.gruber@usi.ch
    """

# ========= Utility functions for accounts and credentials ==========

def load_credentials():
    import os, json
    filename = '..'+os.path.sep+'..'+os.path.sep+'credentials'
    with open(filename) as json_file:
        cred = json.load(json_file)
    return(cred)

def generate_account_dict():
    from algosdk import account, mnemonic
    private_key = account.generate_account()[0]    # need [0], because generate_account() returns a list
    acc = {}
    acc['public'] = account.address_from_private_key(private_key)
    acc['private'] = private_key
    acc['mnemonic'] = mnemonic.from_private_key(private_key)
    return acc

def send_payment(client, sender_private, receiver_public, amount, note=''):
    # client = algosdk client
    # sender_private = private key of sender
    # receiver_public = public address of sender
    # amount = amount in ALGOs
    # note = note as encoded JSON (if any)
    from algosdk import account
    from algosdk.v2client import algod
    from algosdk.future.transaction import PaymentTxn
   
    sp             = client.suggested_params()
    algo_precision = 1e6
    sender_public  = account.address_from_private_key(sender_private)
    amount_microalgo = int(amount * algo_precision)

    unsigned_txn = PaymentTxn(sender_public, sp, receiver_public, amount_microalgo, None, note)
    
    signed_txn = unsigned_txn.sign(sender_private)
    txid = client.send_transaction(signed_txn)
    return(txid)


# ========= Utility functions for transactions ==========

def wait_for_confirmation(client, txid):
    # client = algosdk client
    # txid = transaction ID, for example from send_payment()
    
    # TODO: improve to work with groups
    from algosdk import account
    from algosdk.v2client import algod
    
    if txid is None:
        print("Empty transaction id.")
        return None
    else:
        current_round = client.status()["last-round"]        # obtain last round number
        print("Current round is  {}.".format(current_round))
        txinfo = client.pending_transaction_info(txid)       # obtain transaction information
   
        # Wait for confirmation
        while ( txinfo.get('confirmed-round') is None ):            # condition for waiting = 'confirmed-round' is empty
            print("Waiting for round {} to finish.".format(current_round))
            client.status_after_block(current_round)             # this wait for the round to finish
            txinfo = client.pending_transaction_info(txid)    # update transaction information
            current_round += 1
        print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
        return txinfo
    
def note_encode(note_dict):
    import json
    # note dict ... a Python dictionary
    note_json = json.dumps(note_dict)
    note_byte = note_json.encode()     
    return(note_byte)

def note_decode(note_64):
    # note64 =  note in base64 endocing
    # returns a Python dict
    import base64
    
    message_base64 = txinfo['txn']['txn']['note']
    message_byte   = base64.b64decode(message_base64)
    message_json   = message_byte.decode()
    message_dict   = json.loads( message_json )
    return(message_dict)

# ========= Utility functions for working with ASA ==========

def asset_holdings(client, public):
    # client = algosdk client
    # public = public address to be analyzed

    import pandas as pd
    from algosdk.v2client import algod
    account_info = client.account_info(public)

    info = []
    # Algo part
    info.append( {'amount':  account_info['amount']/1E6, 
                  'unit' :   'ALGO', 
                  'asset-id': 0, 
                  'name': 'Algorand',
                  'decimals': 6
                  } )

    # ASA part
    assets = account_info['assets']
    for asset in assets:
        asset_id     = asset['asset-id']
        asset_info   = client.asset_info(asset_id)                         # Get all info
        asset_amount = asset['amount']/10**asset_info['params']['decimals']      # convert to BIG units
        asset_unit   = asset_info['params']['unit-name']
        info.append( {'amount':  asset_amount,
                      'unit' :   asset_unit,
                      'asset-id':asset_id,
                      'name': asset_info['params']['name'],
                      'decimals': asset_info['params']['decimals']
                      } )
    return(info) #.sort_values('asset-id')

def asset_holdings_df(client, public):
    # client = algosdk client
    # public = public address to be analyzed
    import pandas as pd
    from algosdk.v2client import algod
    info = asset_holdings(client, public)
    df = pd.DataFrame(info)
    return(df)

def asset_holdings_df2(client,adr1,adr2,suffix=['','']):
    # client = algosdk client
    # adr1, adr2 = public address to be analyzed
    import pandas as pd
    from algosdk.v2client import algod
    info1 = asset_holdings(client, adr1)
    df1 = pd.DataFrame(info1)
    info2 = asset_holdings(client, adr2)
    df2 = pd.DataFrame(info2)
    pd.set_option('precision', 4)
    df_merge = pd.merge(df1,df2,how="outer", on=["asset-id", "unit", "name", "decimals"],suffixes=suffix)
    return(df_merge)


# ========= Utility functions for stateful smart contracts ==========

def read_global_state(client, app_id):
    # reads an app's global state
    # client = client
    return  client.application_info(app_id)["params"]["global-state"]

def read_local_state(client, addr, app_id):
    # reads a user's local state
    # client = client
    # addr = public addr of the user that we want to inspect
    results = client.account_info(addr)
    for local_state in results["apps-local-state"]:
        if local_state["id"] == app_id:
            if "key-value" not in local_state:
                return {}
            return format_state(local_state["key-value"])
    return {}

def format_state(state):
    # formats the state (local/global) nicely
    import algosdk
    import base64
    formatted = {}
    for item in state:
        key = base64.b64decode(item["key"]).decode("utf-8")
        value = item["value"]
        if value["type"] == 1:                  # formating of Byteslice variables
            if len(value["bytes"]) == 44:                 # Is it an address? Yes, if length in Bytes is 44
                formatted_value = algosdk.encoding.encode_address(base64.b64decode(value["bytes"]))
            else:                                         # Everything else is considered a text
                formatted_value = base64.b64decode(value["bytes"]).decode("utf-8")            
            formatted[key] = formatted_value
        else:
            formatted[key] = value["uint"]      # formatting of Int variables
    return formatted

# For users: clear private state
def clear_app(client, private_key, app_id):
    sender = account.address_from_private_key(private_key)
    sp = client.suggested_params()
    txn = transaction.ApplicationClearStateTxn(sender, sp, app_id)
    stxn = txn.sign(private_key)
    txid = client.send_transactions([stxn])
    txinfo = wait_for_confirmation(client, txid)
    print("Cleared app-id:", txinfo["txn"]["txn"]["apid"])

# For creators: kill the app
def delete_app(client, private_key, app_id):
    from algosdk import transaction, account
    sender = account.address_from_private_key(private_key)
    sp = client.suggested_params()
    txn = transaction.ApplicationDeleteTxn(sender, sp, app_id)
    stxn = txn.sign(private_key)
    txid = client.send_transactions([stxn])
    txinfo = wait_for_confirmation(client, txid)
    print("Deleted app-id:", txinfo["txn"]["txn"]["apid"])