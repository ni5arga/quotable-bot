import requests
import json
import random
import time
import telegram

# Replace YOUR_TOKEN with your Telegram bot token
bot = telegram.Bot(token='YOUR_TOKEN')

# Quotable API URL
url = "https://api.quotable.io/random"

# Send a random quote to the user
def send_quote(chat_id):
    response = requests.get(url)
    data = json.loads(response.text)
    quote = data['content']
    author = data['author']
    message = f"{quote}\n- {author}"
    bot.send_message(chat_id=chat_id, text=message)

# Keep sending quotes every hour
while True:
    # Get a list of all active chats
    chats = bot.get_updates()
    if len(chats) > 0:
        for chat in chats:
            chat_id = chat.message.chat_id
            send_quote(chat_id)
    time.sleep(3600)
