from binance.enums import *
from binance.client import Client
from binance import AsyncClient
from gevent import os
from dotenv import load_dotenv
from utils import *
import asyncio


load_dotenv()


class Connect:

    client = None

    async def create_client(self):
        api_key = os.environ.get('api_key')
        api_secret = os.environ.get('api_secret')
        self.client = AsyncClient(api_key, api_secret, testnet=True)

    async def place_order(self, order_msg="", _type=ORDER_TYPE_LIMIT, _side=SIDE_BUY, _price=1) -> None:
        """
        this places an order, need to change the hardcoded values
        :return:
        """

        order = await self.client.create_order(
            symbol="{0}{1}".format(order_msg["symbol"], order_msg["token"]),
            side=_side,
            type=_type,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=int(order_msg['percentage']),
            price=_price
        )
        print(order)

    async def get_history(self, symbol='XRPBNB') -> None:
        """
        :return:
        """
        orders = await self.client.get_my_trades(symbol=symbol)
        print(orders)

    async def get_balance(self, asset='USDT'):
        """
        :param asset: the tokens we want to check the balance for in our account
        :return:
        """
        balance = await self.client.get_asset_balance(asset=asset)
        print(balance)
        return balance

    async def close_connection(self):
        await self.client.close_connection()


async def main(msg=None):
    # need to replace this msg with the ones from telegram later on
    # temp_msg1 = "buy-XRPBNB-10"
    # temp_msg2 = "sell-ADABTC-20"
    # temp_msg2 = "market buy XRP BUSD 20"
    client = Connect()
    await client.create_client()
    _balance = await client.get_balance('BUSD')

    order_msg = await parse_message(msg, _balance)
    print("order msg: ", order_msg)

    await client.place_order(order_msg, _type=ORDER_TYPE_LIMIT, _side=SIDE_BUY)
    await client.get_history("{0}{1}".format(order_msg["symbol"], order_msg["token"]))
    await client.get_balance(order_msg["token"])
    await client.close_connection()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
