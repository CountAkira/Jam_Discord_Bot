import mysql.connector
from Config.serverConfig import serverConfig

def getDBCursor():
    """
    Connects to the MySQL database using config.json settings
    and returns a connection and cursor.
    """
    mysql_config = serverConfig["mySql"]

    connection = mysql.connector.connect(
        host=mysql_config['host'],
        user=mysql_config['user'],
        password=mysql_config['password'],
        database=mysql_config['database']
    )

    return connection, connection.cursor()