from brownie import moodien-token
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

def main():
    accout = get_account()
    mdn_token= moodien-token