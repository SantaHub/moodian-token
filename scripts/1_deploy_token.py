from brownie import MDNToken
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
from scripts.helpful_scripts import get_account
from web3 import Web3


initial_supply = Web3.toWei(1000, "ether")

gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)

gas_price(gas_strategy)


def main():
    account = get_account()
    mdk_token = MDNToken.deploy(initial_supply, {"from": account, "gas_price": gas_strategy})
    print(mdk_token.name())
