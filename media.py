import bot
import discord
from discord.ext.commands import Bot
pybot = Bot(command_prefix = "!")

@pybot.group(pass_context=True, aliases='m')
async def media(context):
    song_que = ['https://www.youtube.com/watch?v=WX-vAs__3YA', 'https://www.youtube.com/watch?v=wsrPWMeYPxY', 'https://youtu.be/URiDdlAS6ls']
    playing = ['name', 'url']
    voice = await bot.pybot.join_voice_channel(channel=bot.findchannel(context))
    player = await voice.create_ytdl_player(url=song_que[0])
    media.player.start()

@media.command(aliases='s')
async def stop():
    media.player.stop()

@media.command(aliases='p')
async def pause():
   media.player.pause()

@media.command(aliases='r')
async def resume():
    media.player.resume()

@media.command(aliases='q')
async def que(*url):
    pass

@media.command(aliases='vol')
async def volume(vol_num):
    vol_num = float(vol_num)/100
    media.player.volume(vol_num)