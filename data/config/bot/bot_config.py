import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')

PARSE_MODE = 'HTML'

DISABLE_WEB_PAGE_PREVIEW = False

SKIP_UPDATES = True
