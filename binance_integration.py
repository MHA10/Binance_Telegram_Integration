from config import Connect
import json
from json import loads, JSONDecodeError
from time import sleep
import websocket


def connect():
    client = Connect().make_connection()
    print("logged in")


def binance():
    connect()

    def on_message(ws, message):
        try:
            data = json.loads(message)
        except JSONDecodeError:
            data = {}

        print(message)

    def ws_open(ws):
        # waiting for the authentication
        sleep(3)
        # subscribe_spot_price(ws)
        # subscribe_trade_price(ws)

        return

    endpoint = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
    ws = websocket.WebSocketApp(endpoint, on_open=ws_open, on_message=on_message)
    ws.run_forever()


if __name__ == '__main__':
    binance()
