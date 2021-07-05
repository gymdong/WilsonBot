import discord
from discord import guild
from discord.mentions import AllowedMentions
import requests
import time
from discord.ext import commands
from bs4 import BeautifulSoup

token = "ODU4MzIyNzE1ODMyMzUyODAw.YNcdUg.x0oBUzaP_irR4uSvwK-mOhXXuaE"
ER_KEY = "XsOnGlLvky6sSAOmWZP6F4DVlzHNkiqWaclCzvXl"
ER_URL = "https://open-api.bser.io/v1"
header_params = {"x-api-key": ER_KEY}

client = commands.Bot(command_prefix='!')


def whereItem(item):
    html = requests.get(
        f"https://eternalreturn.fandom.com/ko/wiki/{item}").text
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("table", "infoboxtable").find("img")["src"]
    try:
        itemDropList = soup.find("table", "sortable").find_all('td')
        embed = discord.Embed(title=f"{item}", color=0x00aaaa)
        embed.set_author(name="『아이템 획득 경로』")
        embed.set_thumbnail(url=f"{image}")

        for i in range(0, 100, 2):
            try:
                embed.add_field(
                    name=f"{itemDropList[i].find('a')['title']}", value=f"{itemDropList[i+1].text}")
            except:
                break
    except:
        itemDropList = soup.find(
            'div', 'mw-parser-output').select('p')[1].text
        embed = discord.Embed(
            title=f"{item}", description=f"{itemDropList}", color=0x00aaaa)
        embed.set_author(name="『아이템 획득 경로』")
        embed.set_thumbnail(url=f"{image}")
    return embed


def killItem(item):
    html = requests.get(
        f"https://eternalreturn.fandom.com/ko/wiki/{item}").text
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.find("table", "infoboxtable").find("img")["src"]
    itemKillList = soup.select("table.sortable")[1].find_all('td')
    embed = discord.Embed(title=f"{item}", color=0x00aaaa)
    embed.set_author(name="『아이템 획득 경로』")
    embed.set_thumbnail(url=f"{image}")

    for i in range(0, 100, 2):
        try:
            embed.add_field(
                name=f"{itemKillList[i].find('a')['title']}", value=f"{itemKillList[i+1].text}")
        except:
            break
    return embed


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="실험중입니다."))
    print("I'm ready!")
    print(client.user.name)
    print(client.user.id)
    return


@client.event
async def on_guild_join(guild):
    try:
        channel = await guild.create_text_channel("이터널리턴 위키")
        await channel.send("@everyone 방이 생성되었습니다~", allowed_mentions=discord.AllowedMentions(everyone=True))
    except:
        await guild.system_channel.send("관리자 권한을 주시고 !newroom을 입력하세요~")
    return


@client.command(pass_context=True)
async def abc(ctx, *, arg):
    await ctx.send(f"안녕하세요{arg}")
    return


@client.command()
async def newroom(ctx):
    channel = await ctx.guild.create_text_channel("이터널리턴 위키")
    await channel.send("@everyone 방이 생성되었습니다~ 여기서 위키를 이용해 주세요!", allowed_mentions=discord.AllowedMentions(everyone=True))
    return


@client.command(aliases=['아이템드랍'])
async def Info(ctx, *, arg):
    try:
        embed = whereItem(arg)
        await ctx.send(embed=embed)
    except:
        await ctx.send("없는 아이템인 것 같네요.")
    return


@client.command(aliases=['아이템사냥'])
async def Kill(ctx, *, arg):
    try:
        embed = killItem(arg)
        await ctx.send(embed=embed)
    except:
        await ctx.send("없는 아이템이거나 사냥에서 나오지 않는 아이템인가봐요.")
    return


@client.command(aliases=['루트'])
async def Route(ctx, *, arg):
    await ctx.send("루트정보")
ER_URL_DATA = ER_URL
client.run(token)
