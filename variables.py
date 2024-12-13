from dotenv import load_dotenv

import os
import re


load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')

EMAIL_PATTERN = re.compile('[0-9a-zA-z]+@[0-9a-zA-z]+\.[0-9a-zA-z]+')

SMTP_HOST = 'smtp.yandex.ru'
SMTP_PORT = 587

EMAIL_LOGIN = os.getenv('EMAIL_LOGIN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
