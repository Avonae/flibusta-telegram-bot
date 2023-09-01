# Тестовый сайт
'''
from bs4 import BeautifulSoup
from requests import get
page = get("https://www.kompas.com/ramadhan/jadwal-imsakiyah")
soup = BeautifulSoup(page.text, "lxml")

option = soup.find("select", {"name": "state"}).findAll("option")
daerah = []
for i in option:
    name = i.text
    link = i["value"]
daerah.append({
    "province": name,
    "link": link
})
# print(daerah)
# print(*daerah, sep="\n")

print(option)
print(option)
'''

# Flibusta
import tempfile
from typing import Optional
import aiohttp
import fake_useragent
from aiogram import types
from aiohttp import TCPConnector
from bs4 import BeautifulSoup
from requests import get
# from import config


page = get("http://flibusta.is/b/77882")
soup = BeautifulSoup(page.data, 'lxml')
print(soup.select_one('select[name="financingType"]').select_one(
    'option[select="select"]').text)

print(soup.select_one('option[select="select"]')['value'])
print(soup.select_one('option[select="select"]').text)

#print(results)


'''
option_tags = soup.find_all('option')  # Find All Options Tag
for option_tag in option_tags:
    value = option_tag['value']
    print(value)
    

'''
# soup = BeautifulSoup(page.text, "lxml")

# option = soup.find("select", {"name": "dtp"})
# print(spisok.prettify())
# print(results)
# print(option)
'''
import requests
main_site = requests.get("https://www.ariva.de/ether-kurs/historische_kurse")
soup = BeautifulSoup(main_site.content, 'html.parser')
website = soup.find(attrs={'id': 'WEBSEITE'})
select = website.find(attrs={'name': 'month'})
option = select.find_all('option')
print(option)
'''
