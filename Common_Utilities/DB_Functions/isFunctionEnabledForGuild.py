import mysql.connector

def isFunctionEnabledForGuild(cursor: mysql.connector.cursor.MySQLCursor, function_name: str, guild_id: int) -> bool:
    """
    Checks if a given guild_id is associated with the specified function_name
    in the guild_enabled_functions table.

    Args:
        cursor (MySQLCursor): The MySQL cursor object.
        function_name (str): The function name to look up.
        guild_id (int): The guild ID to check.

    Returns:
        bool: True if the guild_id is enabled for the function_name, False otherwise.
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
        return str(guild_id) in [gid.strip() for gid in guild_ids if gid.strip().isdigit()]
    else:
        return False
