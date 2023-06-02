from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from dotenv import load_dotenv

from time import sleep
import os

ENV_DIR = os.path.join(os.getcwd(),".env")
load_dotenv(ENV_DIR)

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
name = os.environ.get("PHONE")
client = TelegramClient(name, api_id, api_hash)


async def main():
    a =  open("logins.txt","r").read().split("\n")
    b = [x.replace("@","") for x in a]
    for zi,user in enumerate(b[130:]):
        # sleep(1)
        try:
            await client(InviteToChannelRequest(-1001770866716,[user]))
            print(zi,":","Приглашен",user)
        except FloodWaitError as e:
            print("Waiting",e.seconds)
            sleep(int(e.seconds)+60)
        except Exception as e:
            print("Не прошел ",user)

with client:
    client.loop.run_until_complete(main())