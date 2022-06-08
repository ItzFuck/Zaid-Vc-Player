import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from config import API_HASH, API_ID, BOT_TOKEN
SESSION_NAME = None
from pyrogram import Client
from pytgcalls import PyTgCalls

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)

BOT = TelegramClient('BOT', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

user = None

Test = None
call_py = None
