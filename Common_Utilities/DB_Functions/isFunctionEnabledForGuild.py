from Common_Utilities import getDBCursor

def isFunctionEnabledForGuild(function_name: str, guild_id: int) -> bool:
    """
    Checks if a given guild_id is associated with the specified function_name
    in the guild_enabled_functions_by_guild table and is enabled.

    Args:
        function_name (str): The function name to look up.
        guild_id (int): The guild ID to check.

    Returns:
        bool: True if the guild_id is enabled for the function_name, False otherwise.
    """
    connection, cursor = getDBCursor()

    try:
        query = """
            SELECT 1
            FROM guild_enabled_functions_by_guild
            WHERE function_name = %s AND guild_id = %s AND is_enabled = TRUE
            LIMIT 1;
        """

        cursor.execute(query, (function_name, str(guild_id)))
        result = cursor.fetchone()
        return result is not None

    finally:
        cursor.close()
        connection.close()
