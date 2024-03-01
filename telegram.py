import sys
import time
import telepot
import json
import re
from op_webscraping_test import webscraping
from telepot.loop import MessageLoop


with open("tokens.json", "r") as f:
    TOKEN = json.load(f)["telegram_token"]

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        bot.sendMessage(chat_id, "Please, send a picture and a description of what you would like Gemini to do with it")

#TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)