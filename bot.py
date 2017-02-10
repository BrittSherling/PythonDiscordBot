import logging
import secrets
import media
import requests
import discord
from discord.ext.commands import Bot

pybot = Bot(command_prefix = "!")
# discord.opus.load_opus
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

@pybot.command(pass_context=True)
async def truck(context):
    return await pybot.say(context.message.author.mention+' Watchout for that truck')

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
    if discord.opus.is_loaded:
        await pybot.join_voice_channel(channel=findchannel(context))
    pybot.say('opus voice not loaded')

@pybot.command(pass_context=True)
async def m(context):
    media.media(context)

def findchannel(context):
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
                    return channel
pybot.run(secrets.BOT_TOKEN)