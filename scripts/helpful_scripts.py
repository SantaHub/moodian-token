from brownie import accounts, network, config

LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache",
    "hardhat",
    "local-ganache",
    "mainnet-fork",
]
# 0xBD033240B65134afE70C2640E1009718A611EbE0

# 0x66aB6D9362d4F35596279692F0251Db635165871

def get_account(index=None, id=None):
    if id:
        return accounts.load(id)
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(accounts[0].balance())
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

# brownie accounts new moodianACC1
# 606998722ee4071b166810215edb17ee622ac07376c6cbf82017ade554de0abc