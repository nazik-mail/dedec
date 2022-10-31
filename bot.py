import asyncpraw
import asyncio
import config
from aiogram import Bot, types

API_TOKEN = config.settings['TOKEN']
CHANNEL_ID = -1001848387955

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                     client_secret=config.settings['SECRET_CODE'],
                     user_agent='random_raddit_bot/0.0.1')
           
mems = []          
TIMEOUT - 5
SUBREDDIT_NAME = 'lolopdcd'
POST_LIMIT = 1

async def send_messange(channel_id: int, text: str):
    await bot.send_messange(channel_id, text)

async def main():
    while True:
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit=POST_LIMIT)
        item = await memes_submissions.__anext__()
        if item.title not in mems:
            mems.append(item.title)
            await send_messange(CHANNEL_ID, item.url)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())


    