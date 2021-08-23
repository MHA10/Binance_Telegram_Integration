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

    def place_order(self, order_msg="", _type='limit') -> None:
        """
        this places an order, need to change the hardcoded values
        :return:
        """

        if order_msg["side"] == "buy":
            # asset = order_msg["symbol"]
            # balance = self.get_balance(asset)
            # available = balance["free"]
            # percentage = int(msg_dict["percentage"])

            checked_quantity = 0
            if _type == 'limit':
                order = self.client.order_limit_buy(
                        symbol="{0}{1}".format(order_msg["symbol"], order_msg["token"]),
                        quantity=order_msg['percentage'],
                        price=1)
            if _type == 'market':
                order = self.client.order_market_buy(
                        symbol="{0}{1}".format(order_msg["symbol"], order_msg["token"]),
                        quantity=order_msg['percentage'])

            print(order)

    def get_history(self, symbol='XRPBNB') -> None:
        """
        :return:
        """
        orders = self.client.get_my_trades(symbol=symbol)

        print(orders)

    def get_balance(self, asset='USDT'):
        """
        :param asset: the tokens we want to check the balance for in our account
        :return:
        """
        balance = self.client.get_asset_balance(asset=asset)
        print(balance)
        return balance


if __name__ == '__main__':
    # need to replace this msg with the ones from telegram later on
    # temp_msg1 = "buy-XRPBNB-10"
    # temp_msg2 = "sell-ADABTC-20"
    temp_msg2 = "buy XRP USDT 20"
    order_msg = parse_message(temp_msg2)
    client = Connect()
    # place_order(client)
    client.get_balance('USDT')
    client.place_order(order_msg)
    client.get_history()
    client.get_balance('USDT')
