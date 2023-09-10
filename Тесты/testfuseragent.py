import tempfile
from typing import Optional

import aiohttp
from fake_useragent import UserAgent
from aiogram import types
from aiohttp import TCPConnector
from bs4 import BeautifulSoup

import config

import requests
ua = UserAgent()
# куда шлем (этот URL как раз ответит нам наш UA для проверки)
url = 'https://httpbin.org/user-agent'
# создаем заголовок
headers = {'User-Agent': ua.random}
# делаем запрос, передав заголовок
result = requests.get(url, headers=headers)
print(result.content)
