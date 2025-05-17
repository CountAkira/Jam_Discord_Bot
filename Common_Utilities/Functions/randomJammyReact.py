import discord

async def randomJammyReact(message):
    random1 = 0
    count = count + 1
    random1 = random.randint(0, 1000)
    
    if(random1 == 1 or count > 1000):
        count = 0
        valle = '<:valle:900498352263807018>'
        flush = '<:OmegaFlushed:904878039777820702>'
        jomlife = '<:jomLife:925236021187182592>'
        ayaya = '<:ayaya:898723357678264350>'
        pog = '<:pog:898722897407909959>'
        jom = '<:jomseph:898722577554497568>'
        
        random2 = random.randint(0, 5)
        #print('random number 2')
        #print(random2)
        
        if(random2 == 0):
            await message.add_reaction(valle)
        elif(random2 == 1):
            await message.add_reaction(flush)
        elif(random2 == 2):
            await message.add_reaction(jomlife)
        elif(random2 == 3):
            await message.add_reaction(ayaya)
        elif(random2 == 4):
            await message.add_reaction(pog)
        elif(random2 == 5):
            await message.add_reaction(jom)