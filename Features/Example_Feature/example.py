import discord
from discord import app_commands
from Common_Utilities import grabGuildListForFunction

def register_example_command(tree: app_commands.CommandTree, mycursor):
    @tree.command(
        name="example",
        description="My first application Command",
        guilds=grabGuildListForFunction(mycursor, "example")
    )
    async def example(interaction: discord.Interaction):
        await interaction.response.send_message("Helloooo!")
