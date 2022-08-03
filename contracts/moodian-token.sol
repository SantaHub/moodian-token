//pragma solidity ^0.5.0;
//
//import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
//import "@openzeppelin/contracts/token/ERC20/ERC20Detailed.sol";
//
//contract GLDToken is ERC20, ERC20Detailed {
//    // wei
//    constructor(uint256 initialSupply) ERC20Detailed("Moodian", "MDN", 18) public {
//        _mint(msg.sender, initialSupply);
//    }
//}


// contracts/MDNToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MDNToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Moodian", "MDN") {
        _mint(msg.sender, initialSupply);
    }
}