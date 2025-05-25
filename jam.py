import discord
import asyncio

from DB_Scripts.dbSetup import initialize_database
from Features.commandLoader import load_all_commands

from Config.config import config

from Common_Utilities import randomJammyPin, randomJammyReact, isFunctionEnabledForGuild, authorize, scheduledEventChecker, updateAllScheduledEventsToToday

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

# Polling for scheduled events that run every minute
# Scheduled events should be in either a daily amount of minutes, an hour amount of minutes, a half hour of minutes, a quarter hour of minutes, a singular minute. 
# Any timings outside of those are at risk of running the event several times if the bot goes down. 
async def scheduled_events_polling():
    await bot.wait_until_ready()  # Ensures the bot is fully logged in before starting
    print("Starting up polling every minute for scheduled events...")
    while not bot.is_closed():
        try:
            await scheduledEventChecker(bot)  # You can pass the bot if your logic needs access to it
        except Exception as e:
            print(f"Error in polling task: {e}")
        await asyncio.sleep(60)  # Wait one minute

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

# Initial function that runs after bot.run(token)
@bot.event
async def on_ready():
    # Uncomment this await tree sync with your guild number and comment out await tree.sync() if you want to update any slash commands you just made
    # Otherwise it will take an hour for discord to update normally
    # Await tree.sync(guild=discord.Object(id=846475513983926273))
    await tree.sync()
    print(f'{bot.user} has connected to Discord.')

    # Updates all scheduled events to the current day
    # This ensures that if the bot is turned off all events will be on the correct date
    updateAllScheduledEventsToToday()

    # Start polling task for scheduled events
    bot.loop.create_task(scheduled_events_polling())

# Start bot
bot.run(config['discord']['botToken'])