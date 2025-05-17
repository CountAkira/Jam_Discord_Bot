import mysql.connector
import json
from typing import Any
from Common_Utilities import getDBCursor

def setCustomVariable(
    guild_id: int,
    var_name: str,
    var_value: Any
) -> None:
    """
    Inserts or updates a custom variable for a guild in the custom_variables table.

    Args:
        conn (MySQLConnection): The active MySQL database connection.
        guild_id (int): The guild ID.
        var_name (str): The name of the variable.
        var_value (Any): The value to store (will be serialized as JSON).
    """
    connection, cursor = getDBCursor()
    
    query = """
        INSERT INTO custom_variables (guild_id, var_name, var_value)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE var_value = VALUES(var_value);
    """

    try:
        json_value = json.dumps(var_value)
        cursor.execute(query, (guild_id, var_name, json_value))
        connection.commit()
    finally:
        cursor.close()
        connection.close()