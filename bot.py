import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5724313197:AAGxRV4Bi92FHUtIpL4EfV9QPY4sdVs5wP0")

API_ID = int(os.environ.get("API_ID", "10165788"))

API_HASH = os.environ.get("API_HASH", "171d9bdd25a97f140b6be525ec33f8fb")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
