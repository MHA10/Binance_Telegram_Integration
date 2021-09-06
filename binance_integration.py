from binance.enums import *
from binance.client import Client
from binance import AsyncClient
from gevent import os
from dotenv import load_dotenv
from utils import *
import asyncio
from binance import ThreadedWebsocketManager


load_dotenv()


class BinanceClass:

    client = None

    async def create_client(self):
        api_key = os.environ.get('api_key')
        api_secret = os.environ.get('api_secret')
        self.client = AsyncClient(api_key, api_secret, testnet=True)

    async def place_order(self, sym, token, side, percent, _type, prc=1) -> None:
        try:
            order = await self.client.create_order(
                symbol=f"{sym}{token}",
                side=side,
                type=_type,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=int(percent),
                price=prc
            )
        except Exception as e:
            # need to log this error
            return e
        print(order)
        return 'order placed successfully'

    async def get_history(self, sym, token) -> None:
        orders = await self.client.get_my_trades(symbol=f"{sym}{token}")
        print(orders)

    async def get_balance(self, token) -> str:
        balance = await self.client.get_asset_balance(asset=token)
        print(balance)
        return balance

    async def close_connection(self):
        await self.client.close_connection()

    async def parse_message(self, msg):
        """
        EXPECTED MSG: market buy xrp usdt 10
        NOTATION: {type} {side} {symbol} {token} {percentage}
        :return: dict
        """
        order_details = msg.split(' ')
        try:
            order_msg = {
                'type': order_details[0].upper(),
                'side': order_details[1].upper(),
                'symbol': order_details[2].upper(),
                'token': order_details[3].upper(),
            }

            token = order_msg.get('token', None)
            if token is not None:
                _balance = await self.get_balance(token)
                print(_balance)
            else:
                return {'error': 'invalid token not passed'}

            order_msg['percentage'] = (float(order_details[4]) * 0.01) * float(_balance['free'])
        except Exception as e:
            # in case of error we return what error did we get
            return {'error': e}

        return order_msg


async def main(msg, user):
    client_obj = BinanceClass()
    await client_obj.create_client()

    order_msg = await client_obj.parse_message(msg)
    print("order msg: ", order_msg)

    _type = order_msg.get('type', None)
    side = order_msg.get('side', None)
    symbol = order_msg.get('symbol', None)
    token = order_msg.get('token', None)
    percentage = order_msg.get('percentage', None)
    error = order_msg.get('error', None)

    if user == 'user' and side == SIDE_BUY:
        return 'Users are not allowed to buy'

    if error is not None:
        # send error message as response
        await client_obj.close_connection()
        return 'An error occured'
    if _type not in (ORDER_TYPE_LIMIT, ORDER_TYPE_MARKET):
        error = 'Please enter {market or limit order only}!'
        await client_obj.close_connection()
        return error
    if side not in (SIDE_BUY, SIDE_SELL):
        error = 'Please enter {buy or sell order only}!'
        await client_obj.close_connection()
        return error

    order_status = await client_obj.place_order(sym=symbol, token=token, side=side, percent=percentage,
                                                # _type=_type,
                                                _type=ORDER_TYPE_LIMIT, prc=1)

    await client_obj.get_history(sym=symbol, token=token)
    await client_obj.get_balance(token=token)
    await client_obj.close_connection()

    return order_status
