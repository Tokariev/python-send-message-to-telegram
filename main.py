# 1. Create a bot in BotFather and get the token
# 2. Create a group and add the bot to the group
# 3. Get chat chat ID: https://api.telegram.org/bot{BOT_TOKEN}/getUpdates

import asyncio
import telegram
from secret import bot_token, chat_id

async def send_message(text):
    bot = telegram.Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == '__main__':
    asyncio.run(send_message('Message!'))