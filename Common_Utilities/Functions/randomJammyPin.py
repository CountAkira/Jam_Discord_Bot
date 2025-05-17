import discord
import random

from Config.config import config
from Common_Utilities import setCustomVariable, getCustomVariable

async def randomJammyPin(message):
    randomPin = random.randint(0, 70000)
    pinCount = getCustomVariable(message.guild.id, "pinCount")

    if(pinCount is None):  
        setCustomVariable(message.guild.id, "pinCount", {"count": 0})
        pinCount = {"count": 0}
    
    setCustomVariable(message.guild.id, "pinCount", {"count": pinCount["count"] + 1})

    if(randomPin == 1 or pinCount["count"] > 70000):
        setCustomVariable(message.guild.id, "pinCount", {"count": 0})
        await message.add_reaction('📌')
        await message.channel.send("You have been blessed by Jam-Chan <3", reference=message)