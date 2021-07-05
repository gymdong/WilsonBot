import discord
from discord import guild
from discord.mentions import AllowedMentions
import requests
import time
from discord.ext import commands
from bs4 import BeautifulSoup

html = requests.get(
    "https://eternalreturn.fandom.com/ko/wiki/%EC%9E%AC%EB%A3%8C").text
soup = BeautifulSoup(html, 'html.parser')
a = soup.find('tbody').find_all("a")
for i in range(1, 100):

    print(a[i].text)
"""for i in range(0, 100, 1):
    try:
        print(itemDropList[i].find('a')['title'], itemDropList[i+1].text)
    except:
        break"""
