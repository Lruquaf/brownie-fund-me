from brownie import exceptions, accounts, network
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    fund_me = deploy_fund_me()
    account = get_account()
    entrance_fee = fund_me.getEntranceFee() + 100
    print(entrance_fee)
    print("funding...")
    tx1 = fund_me.fund({"from": account, "value": entrance_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    print("withdrawing...")
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_can_only_owner_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing!")
    fund_me = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": accounts[2]})
