# moodian-token


## Compile the token using

```
bronwie compile
```

## Deploy the token using
    brownie run scripts/1_deploy_token.py


## Output

Script : brownie run scripts/1_deploy_token.py
Brownie v1.19.0 - Python development framework for Ethereum

Compiling contracts...
Solc version: 0.8.0
Optimizer: Enabled  Runs: 200
EVM Version: Istanbul
Generating build data...
- OpenZeppelin/openzeppelin-contracts@4.7.2/ERC20
- OpenZeppelin/openzeppelin-contracts@4.7.2/IERC20
- OpenZeppelin/openzeppelin-contracts@4.7.2/IERC20Metadata
- OpenZeppelin/openzeppelin-contracts@4.7.2/Context
- MDNToken

MoodianTokenProject is the active project.
/Users/austinblaise/.local/pipx/venvs/eth-brownie/lib/python3.9/site-packages/brownie/network/main.py:44: BrownieEnvironmentWarning: Development network has a block height of 429
warnings.warn(
Attached to local RPC client listening at '127.0.0.1:8545'...

Running 'scripts/1_deploy_token.py::main'...
999830675860000000000
0xF4D3CF4B28DE54EaCb78fDdc593D3FE3a509caB3
Transaction sent: 0x22abb90906b7f757e3e0e8ba068b8fa336b56afb121a4ae9c988237a1e1cf688
Gas price: 60.0 gwei   Gas limit: 30000000   Nonce: 7
MDNToken.constructor confirmed   Block: 430   Gas used: 666764 (2.22%)
MDNToken deployed at: 0x701e583647F55b04b71A5544b5bBDAa8d3CD53C2

Moodian
Transaction sent: 0xdfb1e9be490e55822164e23a7f0eb3ec04144a4528f3467a868297ac2a4e8a69
Gas price: 60.0 gwei   Gas limit: 30000000   Nonce: 8
MDNToken.transfer confirmed   Block: 431   Gas used: 51671 (0.17%)


## Referred Videos

https://www.youtube.com/watch?v=Yw0jkDPLqJ8&t=768s