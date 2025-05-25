import requests
from Config.serverConfig import serverConfig

async def fumoDaily(bot, config):
    try:
        request = requests.get('https://www.googleapis.com/youtube/v3/search?key='+serverConfig["YOUTUBE"]["token"]+'&part=snippet&order=date&type=video&videoDuration=short')
        print(request.text)
        bot.get_channel()
        await bot.channel.send('Fumo Fumo <a:cirBoogie:1206477135833997312>')
        await bot.channel.send('https://www.youtube.com/watch?v='+str(request.json()["items"][0]["id"]["videoId"]))
    except KeyError:
        return bot.channel.send("Could not grab videos from our savior Reimu :(")
