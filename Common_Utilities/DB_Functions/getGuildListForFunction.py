import mysql.connector
from typing import List
import discord
from Common_Utilities import getDBCursor  

def getGuildListForFunction(function_name: str) -> List[discord.Object]:
    """
    Retrieves the list of guilds associated with a given function_name
    from the guild_enabled_functions_by_guild table, where is_enabled is True.
    
    Returns them as discord.Object instances.

    Args:
        function_name (str): The function name to look up.

    Returns:
        List[discord.Object]: A list of discord.Object instances representing guilds.
    """
    connection, cursor = getDBCursor()

    try:
        query = """
            SELECT guild_id
            FROM guild_enabled_functions_by_guild
            WHERE function_name = %s AND is_enabled = TRUE;
        """
        cursor.execute(query, (function_name,))
        results = cursor.fetchall()
        return [discord.Object(id=int(row[0])) for row in results]

    finally:
        cursor.close()
        connection.close()
