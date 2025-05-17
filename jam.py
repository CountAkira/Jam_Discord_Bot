import discord
import json
from discord import app_commands
from DB_Scripts.dbSetup import initialize_database
from Features.commandLoader import load_all_commands

from Common_Utilities.Functions import randomJammyPin, randomJammyReact

# Set up discord py basic settings
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

# Load config
with open('Config/config.json', 'r') as file:
    config = json.load(file)

# Initialize database and run SQL scripts
mydb, mycursor = initialize_database(config)

# Register all commands with the prefix register_ in the features folder
load_all_commands(tree, mycursor)

# Initial function that runs after bot.run(token)
@bot.event
async def on_ready():
    #uncomment this await tree sync with your guild number and comment out await tree.sync() if you want to update any slash commands you just made
    #otherwise it will take an hour for discord to update normally
    #await tree.sync(guild=discord.Object(id=896438391040770068))
    await tree.sync()
    print(f'{bot.user} has connected to Discord.')

@bot.event
async def on_message(message):
    print("test1")
    print(message.author.id)
    print(config['bot_information']['user_id'])
    if message.author.id != config['bot_information']['user_id']:
        print("test2")
        #await randomJammyReact(message);
        #await randomJammyPin(message);

# Start bot (must be last)
bot.run(config['discord']['botToken'])