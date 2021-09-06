import sys
from telethon.sync import events
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

        if event.message.sender_id == api_id:
            # the trader messaged!, place both order sides
            user = 'trader'
        else:
            # the user messaged the trader
            user = 'user'
        return_msg = await binance_integration.main(event.message.to_dict()['message'], user)
        await event.reply(return_msg)
# 1941036469
# InputPeerUser(user_id=1941036469, access_hash=2952108563083146034)
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
