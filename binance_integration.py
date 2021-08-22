from binance.enums import *
from binance.client import Client
from gevent import os
from dotenv import load_dotenv
from utils import *

load_dotenv()


class Connect:

    client = None

    def __init__(self, api_key=None, api_secret=None) -> None:
        """
        we can pass in the api_keu and the api_secret key when we move onto the telgeram parsing part
        :param api_key:
        :param api_secret:
        """
        api_key = os.environ.get('api_key')
        api_secret = os.environ.get('api_secret')
        self.client = Client(api_key, api_secret, testnet=True)

    def place_order(self, msg_dict="") -> None:
        """
        this places an order, need to change the hardcoded values
        :return:
        """

        if msg_dict["buy_or_sell"] == "buy":
            asset = (msg_dict["symbol"])[-3:]
            balance = self.get_balance(asset)
            available = balance["free"]
            percentage = int(msg_dict["percentage"])
            print(available)

            checked_quantity = 0
            order = self.client.order_market_buy(
                    symbol=msg_dict["symbol"],
                    quantity=100)


    def get_history(self) -> None:
        """
        this is not working yet
        :return:
        """
        orders = client.get_my_trades(symbol='XRPBNB')

        orders

    def get_balance(self, asset='BTC'):
        """
        :param asset: the tokens we want to check the balance for in our account
        :return:
        """
        balance = self.client.get_asset_balance(asset=asset)
        return balance


if __name__ == '__main__':
    # need to replace this msg with the ones from telegram later on
    temp_msg1 = "buy-XRPBNB-10"
    temp_msg2 = "sell-ADABTC-20"
    parsed_msg = parse_message(temp_msg1)
    # this client can be passed the api_key and the api_secret keys
    client = Connect()
    # place_order(client)
    client.place_order(parsed_msg)
    # client.get_history()
    client.get_balance()
