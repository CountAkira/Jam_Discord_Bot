import discord
import random
from Common_Utilities import setCustomVariable, getCustomVariable

async def randomJammyReact(message):
    randomNumberReact = random.randint(0, 1000)

    reactCount = getCustomVariable(message.guild.id, "reactCount")
    print(reactCount)
    if(reactCount is None):  
        setCustomVariable(message.guild.id, "reactCount", {"count": 0})
        reactCount = {"count": 0}
    
    setCustomVariable(message.guild.id, "reactCount", {"count": reactCount["count"] + 1})
    
    if(randomNumberReact == 1 or reactCount["count"] > 5):
        setCustomVariable(message.guild.id, "reactCount", {"count": 0})

        emotes = getCustomVariable(message.guild.id, "customReactEmotes")

        print(emotes)

        if emotes and isinstance(emotes, list) and len(emotes) > 0:
            # Pick a random emote from the JSON list
            random_emote = random.choice(emotes)
            await message.add_reaction(random_emote)
