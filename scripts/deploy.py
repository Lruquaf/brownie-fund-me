from brownie import FundMe, network, config
from scripts.helpful_scripts import get_account, get_price_feed_address


def deploy_fund_me():
    account = get_account()
    price_feed_address = get_price_feed_address()
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"The contract have deployed at {fund_me}")
    return fund_me


def main():
    deploy_fund_me()
