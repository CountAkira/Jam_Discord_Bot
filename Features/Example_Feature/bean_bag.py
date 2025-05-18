import discord
from discord import app_commands
from Common_Utilities import getGuildListForFunction

def register_bean_bag_command(tree: app_commands.CommandTree):
    @tree.command(
        name="bean_bag",
        description="My first application Command",
        guilds=getGuildListForFunction("bean_bag")
    )
    async def bean_bag(interaction: discord.Interaction):
        await interaction.response.send_message("https://media.discordapp.net/attachments/897922446684991531/1307437246256779275/MV5BMTA2NDE5Njc5MzBeQTJeQWpwZ15BbWU4MDIwNTQxMjEx.png?ex=68299592&is=68284412&hm=7b0c38f9f9f02ba0ed95d76688cdf1030bc60bfea270c09659e125676cebcdda&=&format=webp&quality=lossless&width=1650&height=1086")
