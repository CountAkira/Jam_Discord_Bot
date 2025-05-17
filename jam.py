import discord
import json

from DB_Scripts.dbSetup import initialize_database
from Features.commandLoader import load_all_commands

from Common_Utilities import randomJammyPin, randomJammyReact
from Common_Utilities import grabGuildListForFunction

# Set up discord py basic settings
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)

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
    if message.author.id != config['bot_information']['user_id']:
        print(grabGuildListForFunction(mycursor, "randomJammyPin"))
        #await randomJammyReact(message);
        #await randomJammyPin(message);

# Start bot
bot.run(config['discord']['botToken'])