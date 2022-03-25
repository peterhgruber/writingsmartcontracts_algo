""" oracle.py
Server part of the on-chain oracle
09 Winter School on Smart Contracts
Peter Gruber (peter.gruber@usi.ch)
2022-03-20

# == how to install
(1) install packages
pip3 install pycoingecko
pip3 install py-algorand-sdk
pip3 install pandas

(2) Put this file and credentials_oracle into your home directory
(3) Put algo_util.py into sharedCode
(4) Run with ...
python3 oracle
(test if everything is OK)
(5) Create a cron job to run every 5 minutes (--> this costs 0,288 ALGO per day)
crontab -e
(choose vi)
(inside scroll down and paste the following line, changing the path)
*/5 * * * * cd /home/<yourhomedir>/algo_oracle && python3 oracle.py
(press ctr-X and answer yes)
"""

# ========== Libraries ==========
from pycoingecko import CoinGeckoAPI
import sys, os
from algosdk.future.transaction import Multisig, MultisigTransaction
from algosdk.future.transaction import AssetConfigTxn, AssetTransferTxn, AssetFreezeTxn
from algosdk.v2client import algod
import pandas as pd


# ========== Initialization ==========
# Credentials ... assumed in the same folder as this code
codepath = 'sharedCode'+os.path.sep
sys.path.append(codepath)
from algo_util import *
# additional oracle accounts
cred_oracle = load_credentials('credentials_oracle')
Price = cred_oracle['Price']
Reserve = cred_oracle['Reserve']

# Initialize Purestake API
algod_client = algod.AlgodClient(algod_token='', algod_address=cred_oracle['algod_test'], headers=cred_oracle['purestake_token'])

# Initialize coingecko API
cg = CoinGeckoAPI()

oracle_id = 77534697

# ==========  get current price ==========
price_info = cg.get_price(ids='algorand', vs_currencies='usd')
usdalgo = price_info['algorand']['usd']
# print(usdalgo)

# ==========  get current holdings ==========
# get current holdings
holdings_Price = asset_holdings(algod_client, Price['public'])
oracle_Price = [holding['amount'] for holding in holdings_Price if holding['unit']=='USDALGO'][0]
oracle_Price = int(1e6*oracle_Price)
holdings_Reserve = asset_holdings(algod_client, Reserve['public'])
oracle_Reserve = [holding['amount'] for holding in holdings_Reserve if holding['unit']=='USDALGO'][0]
oracle_Reserve = int(1e6*oracle_Reserve)

print(usdalgo)
print(oracle_Price)
print(oracle_Reserve)

holdings_oracle = int(usdalgo*1e6)

# ==========  Make transfers ==========
holdings_oracle = int(usdalgo*1e6)         # this is how many coins Price *should* hold

# make transfers
if holdings_oracle != oracle_Price:
    # A transaction is needed
    if holdings_oracle > oracle_Price:
        # Price does not have enough coins
        # Reserve needs to transfer to Price
        amt = int(holdings_oracle-oracle_Price)
        sender = Reserve
        receiver = Price
    else:
        # Price has too many coins
        # Price needs to transfer to Reserve
        amt = int(oracle_Price-holdings_oracle)
        sender = Price
        receiver = Reserve

    # === transfer TXN (must be a multisig!!) ===
    # Step 1: prepare
    sp = algod_client.suggested_params()          
    txn = AssetTransferTxn(
        sender = sender['public'],                
        sp=sp,
        receiver=receiver['public'],              
        amt=amt,                                  
        index=oracle_id                          
        )                               

    # Step 2+3: Sign + send
    stxn = txn.sign(sender['private'])
    txid = algod_client.send_transaction(stxn)

    # Step 4: Wait for confirmation
    txinfo = wait_for_confirmation(algod_client, txid)
