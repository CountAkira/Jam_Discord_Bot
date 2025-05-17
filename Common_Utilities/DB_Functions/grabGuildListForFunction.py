import mysql.connector
from typing import List
import discord 

def grabGuildListForFunction(cursor: mysql.connector.cursor.MySQLCursor, function_name: str) -> List[discord.Object]:
    """
    Retrieves the list of guilds associated with a given function_name
    from the guild_enabled_functions table, and returns them as discord.Object instances.

    Args:
        cursor (MySQLCursor): The MySQL cursor object.
        function_name (str): The function name to look up.

    Returns:
        List[discord.Object]: A list of discord.Object instances representing guilds.
    """
    query = """
        SELECT guilds
        FROM guild_enabled_functions
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
