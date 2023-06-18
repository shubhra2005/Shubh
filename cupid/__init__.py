from telethon import TelegramClient 
import logging
import time

openai_key = "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"
api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "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"




bot = TelegramClient("cupidx",api_id,api_hash).start(bot_token = bot_token)
