import discord
from discord import User
from discord.ext.commands import Bot
import urllib as ul
import json
import secrets

pybot = Bot(command_prefix = "!")
client = discord.Client

@pybot.command()
async def hello(*args):
    return await pybot.say("Hello, world!")

@pybot.command()
async def truck(user_id):
    return await pybot.say(user_id+' Watchout for that truck')

@pybot.command()
async def lenny():
    return await pybot.say('( ͡° ͜ʖ ͡°)')

@pybot.command()
async def search(query):
    encoded = ul.parse.quote(query)
    rawData = ul.request.urlopen("https://duckduckgo-duckduckgo-zero-click-info.p.mashape.com/?callback=process_duckduckgo&format=json&no_html=1&no_redirect=1&q={}&skip_disambig=1".format(encoded),
    secrets.headers).read()
    jsonData = json.loads(rawData)
    searchResults = jsonData["Results"]
    print(searchResults)
    return await pybot.say()

pybot.run(secrets.BOT_TOKEN)
