from telethon.sync import TelegramClient, events
from gevent import os
from dotenv import load_dotenv
from telethon import TelegramClient
import binance_integration

load_dotenv()

api_id = os.environ.get('telegram_api_id')
api_hash = os.environ.get('telegram_api_hash')
client = TelegramClient('binance_session', api_id, api_hash)


async def main():
    try:
        await client.connect()
    except Exception as e:
        print('Failed to connect', e, file=sys.stderr)
        return

    @client.on(events.NewMessage())
    async def msg_handler(event):
        await binance_integration.main(event.message.to_dict()['message'])

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
