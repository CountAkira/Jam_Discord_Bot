import discord
import random

from Config.config import config
from Common_Utilities import setCustomVariable, getCustomVariable

async def randomJammyPin(message):
    randomPin = random.randint(0, 70000)
    randomJammyPinCount = getCustomVariable(message.guild.id, "randomJammyPinCount")

    if(randomJammyPinCount is None):  
        setCustomVariable(message.guild.id, "randomJammyPinCount", {"count": 0})
        randomJammyPinCount = {"count": 0}
    
    setCustomVariable(message.guild.id, "randomJammyPinCount", {"count": randomJammyPinCount["count"] + 1})

    if(randomPin == 1 or randomJammyPinCount["count"] > 70000):
        setCustomVariable(message.guild.id, "randomJammyPinCount", {"count": 0})
        await message.add_reaction('📌')
        
        # Get bot nickname or fallback to username
        bot_member = message.guild.get_member(message.guild.me.id)
        bot_name = bot_member.nick if bot_member.nick else bot_member.name

        await message.channel.send(
            f"You have been blessed by {bot_name} <3",
            reference=message
        )