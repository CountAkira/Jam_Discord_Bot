import requests
import discord
from Config.serverConfig import serverConfig

from Common_Utilities import getCustomVariable

async def fumoDaily(bot, config, guild_id):
    fumoDailyChannel = getCustomVariable(guild_id, "fumoDailyChannel")
    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(int(fumoDailyChannel["channel"]))
    try:
        request = requests.get('https://www.googleapis.com/youtube/v3/search?key='+serverConfig["YOUTUBE"]["token"]+'&part=snippet&order=date&type=video&videoDuration=short')
        print(request.text)
        await channel.send('Fumo Fumo '+fumoDailyChannel["emote"])
        await channel.send('https://www.youtube.com/watch?v='+str(request.json()["items"][0]["id"]["videoId"]))
    except Exception as e:
        print(f"[ERROR] An exception occurred in fumoDaily: {e}")
        await channel.send("Could not grab videos from our savior Reimu :(")


