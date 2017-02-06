import discord
from discord import User
from discord.ext.commands import Bot
import secrets
import requests

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
async def search(query):

    respon = requests.get('http://api.duckduckgo.com/?q={}&format=json'.format(query))
    json_object = respon.json()
    result = json_object['Results'][0]['FirstURL']

    return await pybot.say(result)

pybot.run(secrets.BOT_TOKEN)
