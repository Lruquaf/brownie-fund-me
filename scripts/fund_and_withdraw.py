from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print("funding...")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing...")
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)
    print("wthdrawal is successfully!")


def main():
    fund()
    withdraw()
