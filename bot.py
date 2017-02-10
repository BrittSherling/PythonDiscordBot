import logging
import secrets
import requests
import discord
from discord.ext.commands import Bot
from discord import voice_client

pybot = Bot(command_prefix = "!")
discord.opus.load_opus
logging.basicConfig(level=logging.INFO)

@pybot.event
async def on_ready():
    print('Logged in as')
    print(pybot.user.name)
    print(pybot.user.id)
    print('------')

@pybot.command()
async def hello():
    return await pybot.say("Hello, world!")

@pybot.command()
async def truck(user_id):
    return await pybot.say(user_id+' Watchout for that truck')

@pybot.command()
async def lenny():
    return await pybot.say('( ͡° ͜ʖ ͡°)')

@pybot.command(aliases=['s'])
async def search(*q):
    query = {'q': ' '.join(q)}
    respon = requests.get('http://duckduckgo.com/', params=query).url
    return await pybot.say(respon)

@pybot.command(pass_context=True, aliases=['tm'])
async def toMe(context):
    #author of the message
    author = context.message.author
    #id of the author of the message
    author_id = author.id
    #currently connected server
    server = author.server
    #list of channel classes
    channels = server.channels
    if discord.opus.is_loaded:
        for channel in channels:
            for member in channel.voice_members:
                if member.id == author_id:
                    await pybot.join_voice_channel(channel=channel)
    pybot.say('opus voice not loaded')

pybot.run(secrets.BOT_TOKEN)
