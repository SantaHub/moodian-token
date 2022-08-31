from brownie import MDNToken
from brownie.network import gas_price
from brownie.network.gas.strategies import LinearScalingStrategy
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")

# classbrownie.network.gas.strategies.LinearScalingStrategy(initial_gas_price, max_gas_price, increment=1.125, time_duration=30)
gas_strategy = LinearScalingStrategy("60 gwei", "70 gwei", 1.1)


def main():
    account_1 = get_account()
    print(account_1)
    mdk_token = MDNToken.deploy(initial_supply, {"from": account_1, "gas_price": gas_strategy})
    print(mdk_token.name())

    ## Testing transfering tokens
    # transfer_to_account = get_account(index=2)
    # transfer = mdk_token.transfer(transfer_to_account, 99, {'from': account_1, 'gas_price': gas_strategy})

    ## Check if account 2 have the tokens