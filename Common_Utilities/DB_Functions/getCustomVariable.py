import mysql.connector
from typing import Optional, Any
from Common_Utilities import getDBCursor  

def getCustomVariable(
    guild_id: int,
    var_name: str
) -> Optional[Any]:
    """
    Retrieves the var_value for a given guild_id and var_name from the custom_variables table.

    Args:
        guild_id (int): The guild ID.
        var_name (str): The variable name.

    Returns:
        Optional[Any]: The parsed JSON value if found, otherwise None.
    """
    connection, cursor = getDBCursor()

    try:
        query = """
            SELECT var_value
            FROM custom_variables
            WHERE guild_id = %s AND var_name = %s
            LIMIT 1;
        """
        cursor.execute(query, (guild_id, var_name))
        result = cursor.fetchone()
        if result:
            return result[0]  # JSON is already parsed
        return None
    finally:
        cursor.close()
        connection.close()
