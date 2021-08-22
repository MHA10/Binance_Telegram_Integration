from binance.enums import *
from binance.client import Client
from gevent import os
from dotenv import load_dotenv

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

    def place_order(self) -> None:
        """
        this places an order, need to change the hardcoded values
        :return:
        """
        order = self.client.order_market_buy(
                symbol='XRPBNB',
                quantity=100)
        order

    def get_history(self) -> None:
        """
        this is not working yet
        :return:
        """
        orders = client.get_my_trades(symbol='XRPBNB')

        orders

    def get_balance(self, asset='BTC') -> None:
        """
        :param asset: the tokens we want to check the balance for in our account
        :return:
        """
        balance = self.client.get_asset_balance(asset=asset)
        balance


if __name__ == '__main__':
    # binance()

    # this client can be passed the api_key and the api_secret keys
    client = Connect()
    # place_order(client)
    # client.place_order()
    client.get_history()
    client.get_balance()
