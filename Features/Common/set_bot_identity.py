import discord
from discord import app_commands
import aiohttp

def register_set_bot_identity_command(tree: app_commands.CommandTree):
    @tree.command(
        name="set_bot_identity",
        description="Set the bot's nickname, avatar (via URL), and color role in this guild."
    )
    @app_commands.describe(
        nickname="New nickname for the bot in this guild (optional)",
        avatar_url="URL to an image for the bot's avatar (global, optional)",
        hex_color="Hex color code for the bot's role color, e.g. b43d5c or #b43d5c (optional)"
    )
    async def set_bot_identity(
        interaction: discord.Interaction,
        nickname: str = None,
        avatar_url: str = None,
        hex_color: str = None
    ):
        guild = interaction.guild
        if guild is None:
            await interaction.response.send_message("This command can only be used in a server.", ephemeral=True)
            return

        await interaction.response.defer()  # defer for more time

        # Parse hex_color string to int if provided
        hex_color_value = None
        if hex_color:
            hex_color = hex_color.lstrip("#")  # remove leading '#' if present
            try:
                hex_color_value = int(hex_color, 16)
                if hex_color_value < 0 or hex_color_value > 0xFFFFFF:
                    raise ValueError("Color code out of range")
            except ValueError:
                await interaction.followup.send("Invalid hex color code provided. Please use format like 'b43d5c' or '#b43d5c'.", ephemeral=True)
                return

        # Fetch avatar bytes if avatar_url is provided
        avatar_bytes = None
        if avatar_url:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(avatar_url) as resp:
                        if resp.status == 200:
                            avatar_bytes = await resp.read()
                        else:
                            await interaction.followup.send(f"Failed to fetch avatar image: HTTP {resp.status}", ephemeral=True)
                            return
            except Exception as e:
                await interaction.followup.send(f"Error fetching avatar image: {e}", ephemeral=True)
                return

        # 1. Set avatar (global)
        if avatar_bytes:
            try:
                await interaction.client.user.edit(avatar=avatar_bytes)
                print("Bot avatar updated globally.")
            except discord.HTTPException as e:
                print(f"Failed to update avatar (likely rate limited): {e}")
            except Exception as e:
                print(f"Unexpected error updating avatar: {e}")

        # 2. Change bot nickname in the guild
        if nickname is not None:
            try:
                bot_member = guild.get_member(interaction.client.user.id)
                if bot_member is None:
                    await interaction.followup.send("Bot is not a member of this guild.", ephemeral=True)
                    return
                
                await bot_member.edit(nick=nickname)
                print(f"Bot nickname changed to '{nickname}' in {guild.name}")
            except Exception as e:
                print(f"Failed to change bot nickname in {guild.name}: {e}")

        # 3. Set bot's name color via role in the guild
        if hex_color_value is not None:
            try:
                bot_member = guild.get_member(interaction.client.user.id)
                if bot_member is None:
                    await interaction.followup.send("Bot is not a member of this guild.", ephemeral=True)
                    return

                role = discord.utils.get(guild.roles, name="botRoleColor")
                if not role:
                    role = await guild.create_role(name="botRoleColor", color=discord.Color(hex_color_value))
                    print(f"Created role botRoleColor in {guild.name}")

                if role not in bot_member.roles:
                    await bot_member.add_roles(role)
                    print(f"Assigned role botRoleColor to bot in {guild.name}")

                if role.color.value != hex_color_value:
                    await role.edit(color=discord.Color(hex_color_value))
                    print(f"Updated role color in {guild.name}")
            except Exception as e:
                print(f"Failed to update bot name color in {guild.name}: {e}")

        await interaction.followup.send("Bot Identity has been updated!")
