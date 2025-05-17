import discord
from Config.config import config

async def randomJammyPin(message):
    randomPin = random.randint(0, 70000)

    setCustomVariable(connection, guild_id, var_name, var_value)
    
    global pincount
    
    pincount = pincount + 1
    if(randomPin == 1 or pincount > 70000):
        if message.author != bot.user:
            pincount = 0
            await message.add_reaction('📌')
            await message.channel.send("You have been blessed by Jam-Chan <3", reference=message)
        else:
            pincount = 100001