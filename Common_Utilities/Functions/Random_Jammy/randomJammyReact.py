import discord
import random
from Common_Utilities import setCustomVariable, getCustomVariable

async def randomJammyReact(message):
    randomNumberReact = random.randint(0, 1000)

    randomJammyReactCount = getCustomVariable(message.guild.id, "randomJammyReactCount")

    if(randomJammyReactCount is None):  
        setCustomVariable(message.guild.id, "randomJammyReactCount", {"count": 0})
        randomJammyReactCount = {"count": 0}
    
    setCustomVariable(message.guild.id, "randomJammyReactCount", {"count": randomJammyReactCount["count"] + 1})
    
    if(randomNumberReact == 1 or randomJammyReactCount["count"] > 1000):
        setCustomVariable(message.guild.id, "randomJammyReactCount", {"count": 0})

        emotes = getCustomVariable(message.guild.id, "customReactEmotes")

        if emotes and isinstance(emotes, list) and len(emotes) > 0:
            # Pick a random emote from the JSON list
            random_emote = random.choice(emotes)
            await message.add_reaction(random_emote)
