from typing import List
from Common_Utilities import getDBCursor

def getAuthorizationByGuildAndFunctionName(function_name: str, guild_id: str) -> List[str]:
    """
    Retrieves a list of role names/IDs for a specific function and guild from the
    guild_enabled_functions_by_role table. The roles string is split by commas,
    and all whitespace is removed from each resulting entry.

    Args:
        function_name (str): The function name to look up.
        guild_id (str): The Discord guild ID.

    Returns:
        List[str]: A list of cleaned role names or IDs as plain strings.
    """
    connection, cursor = getDBCursor()

    try:
        query = """
            SELECT roles
            FROM guild_enabled_functions_by_role
            WHERE function_name = %s AND guild = %s
            LIMIT 1;
        """
        cursor.execute(query, (function_name, guild_id))
        result = cursor.fetchone()

        if result and result[0]:
            raw_roles = result[0]
            # Split by comma and remove ALL spaces from each entry
            roles = [part.strip().replace(" ", "") for part in raw_roles.split(',')]
            return roles
        else:
            return []

    finally:
        cursor.close()
        connection.close()
