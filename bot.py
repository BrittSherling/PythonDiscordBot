import discord
from discord import User
from discord.ext.commands import Bot
import secrets
import requests
import logging

logging.basicConfig(level=logging.INFO)
pybot = Bot(command_prefix = "!")
client = discord.Client

@pybot.command()
async def hello():
    return await pybot.say("Hello, world!")

@pybot.command()
async def truck(user_id):
    return await pybot.say(user_id+' Watchout for that truck')

@pybot.command()
async def lenny():
    return await pybot.say('( ͡° ͜ʖ ͡°)')

@pybot.command()
async def search(*q):
    query = {'q': ' '.join(q)}
    respon = requests.get('http://duckduckgo.com/', params=query).url
    return await pybot.say(respon)

pybot.run(secrets.BOT_TOKEN)
