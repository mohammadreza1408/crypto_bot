import asyncio
import sys
from clean_data import get_data_clean
from kucoin.client import WsToken,Market
from kucoin.ws_client import KucoinWsClient
from datetime import datetime


#Kucoin WebSocket Get Price
#Spot market

async def main():
    async def deal_msg(msg):
        if msg['topic'] == '/market/snapshot:PAXG-USDT':
            await asyncio.sleep(1)
    client = WsToken()
    ws_client = await KucoinWsClient.create(None, client, deal_msg, private=False)
    await ws_client.subscribe('/market/snapshot:PAXG-USDT')
    while True:
        await asyncio.sleep(60)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

