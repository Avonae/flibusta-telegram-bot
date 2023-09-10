import tempfile
from typing import Optional
import aiohttp
import fake_useragent
from aiogram import types
from aiohttp import TCPConnector
from bs4 import BeautifulSoup
import requests
import config


class Session:
    register_url = 'https://flibusta.is/user'
    data = {
        'name': config.SITE_LOGIN,
        'pass': config.SITE_PASS,
        'form_id': 'user_login'}

    def __init__(self):
        self._user = fake_useragent.UserAgent().random
        self._headers = {'user-agent': self._user}
        self._session: Optional[aiohttp.ClientSession] = None

# Открываем сессию если у нас нет активной
    async def get_session(self) -> aiohttp.ClientSession:
        if self._session is None:
            new_session = aiohttp.ClientSession(
                connector=TCPConnector(verify_ssl=False))
            self._session = new_session
        return self._session

# Закрываем сессию, если она неактивна
    async def close(self) -> None:
        if self._session is None:
            return None
        await self._session.close()

    async def get_soup(self, url: str, chat: types.Chat = None) -> BeautifulSoup:
        '''
        Для запросов из групповых чатов делаем soup с регистрацией на сайте, чтобы были все книги доступны
        '''
        if chat and chat.type == 'private':
            async with self._session.get(url, headers=self._headers) as response:
                return BeautifulSoup(await response.text(), 'lxml')
        else:
            async with self._session.post(self.register_url, headers=self._headers, data=self.data):
                async with self._session.get(url, headers=self._headers) as response:
                    return BeautifulSoup(await response.text(), 'lxml')


# Получаем временный файл

    async def get_tempfile(self, url: str) -> tempfile.TemporaryFile:
        async with self._session.post(self.register_url, headers=self._headers, data=self.data):
            async with self._session.get(url, headers=self._headers) as response:
                if response.status == 200:
                    fp = tempfile.TemporaryFile()
                    fp.write(await response.read())
                    fp.seek(0)
                    return fp
