import discord
import json

from DB_Scripts.dbSetup import initialize_database
from Features.commandLoader import load_all_commands
from Config.config import config

from Common_Utilities import randomJammyPin, randomJammyReact, isFunctionEnabledForGuild, authorize

# Custom CommandTree to hook into slash command execution
class MyCommandTree(discord.app_commands.CommandTree):
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        return await authorize(interaction, interaction.command.name)

# Set up discord basic client
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)
tree = MyCommandTree(bot)

# Initialize database and run SQL scripts
mydb, mycursor = initialize_database(config)

# Register all commands with the prefix register_ in the features folder
load_all_commands(tree)

# Initial function that runs after bot.run(token)
@bot.event
async def on_ready():
    #uncomment this await tree sync with your guild number and comment out await tree.sync() if you want to update any slash commands you just made
    #otherwise it will take an hour for discord to update normally
    #await tree.sync(guild=discord.Object(id=846475513983926273))
    await tree.sync()
    print(f'{bot.user} has connected to Discord.')

# Global check for application commands
@bot.event
async def global_command_check(ctx):
    if isinstance(ctx, discord.ApplicationContext):
        # Run your code before all slash commands here
        print(f"User {ctx.user} invoked {ctx.command.name}")
        # Add more logic as needed
    return True  # Returning False blocks the command

@bot.event
async def on_message(message):
    if message.author.id != config['bot_information']['user_id']:
        if isFunctionEnabledForGuild("randomJammyReact", message.guild.id):
            await randomJammyReact(message);
        if isFunctionEnabledForGuild("randomJammyPin", message.guild.id):
            await randomJammyPin(message);

# Start bot
bot.run(config['discord']['botToken'])