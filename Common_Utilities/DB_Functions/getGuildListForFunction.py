import mysql.connector
from typing import List
import discord
from Common_Utilities import getDBCursor  

def getGuildListForFunction(function_name: str) -> List[discord.Object]:
    """
    Retrieves the list of guilds associated with a given function_name
    from the guild_enabled_functions_by_guild table, and returns them as discord.Object instances.

    Args:
        function_name (str): The function name to look up.

    Returns:
        List[discord.Object]: A list of discord.Object instances representing guilds.
    """
    connection, cursor = getDBCursor()

    try:
        query = """
            SELECT guilds
            FROM guild_enabled_functions_by_guild
            WHERE function_name = %s
            LIMIT 1;
        """
        cursor.execute(query, (function_name,))
        result = cursor.fetchone()

        if result and result[0]:
            guild_ids = result[0].split(',')
            return [discord.Object(id=int(gid.strip())) for gid in guild_ids if gid.strip().isdigit()]
        else:
            return []

    finally:
        cursor.close()
        connection.close()
