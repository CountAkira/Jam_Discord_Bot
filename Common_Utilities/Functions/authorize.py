import discord
from Common_Utilities import getAuthorizationByGuildAndFunctionName

async def authorize(interaction: discord.Interaction, commandName: str) -> bool:
    # Get the member object (user with roles)
    member = interaction.user if isinstance(interaction.user, discord.Member) else await interaction.guild.fetch_member(interaction.user.id)
    
    authorizedRoles = getAuthorizationByGuildAndFunctionName(commandName, str(interaction.guild.id))

    # If authorized roles empty then allow user to use command
    if authorizedRoles == []:
        print(f"[Slash Command] {interaction.user} used {interaction.command.name} and was allowed authorization because there was no auth setting")
        return True

    # Clean the authorized roles list (ensure no extra spaces)
    authorizedRoles = [role.strip().replace(" ", "") for role in authorizedRoles]

    has_role = any(
        str(role.id).replace(" ", "") in authorizedRoles or role.name.replace(" ", "") in authorizedRoles
        for role in member.roles
    )

    if has_role:
        print(f"[Slash Command] {interaction.user} used {interaction.command.name} and was allowed authorization")
        return True
    else:
        print(f"[Slash Command] {interaction.user} used {interaction.command.name} and was denied authorization")
        await interaction.response.send_message("You do not have permission to use this command.", ephemeral=True)
        return False
