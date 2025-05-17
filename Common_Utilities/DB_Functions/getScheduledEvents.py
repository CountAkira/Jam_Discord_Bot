import mysql.connector
from typing import List, Dict, Any
from datetime import datetime, timedelta
from Common_Utilities import getDBCursor 

def getScheduledEvents() -> List[Dict[str, Any]]:
    """
    Retrieves and refreshes scheduled events where event_time <= now.
    Only updates event_time for those exact rows.

    Returns:
        List[Dict[str, Any]]: A list of the original events before refresh.
    """
    connection, cursor = getDBCursor()
    current_time = datetime.utcnow()

    try:
        select_query = """
            SELECT event_name, event_time, guild_id, refresh_time_in_minutes
            FROM scheduled_events
            WHERE event_time <= %s;
        """
        cursor.execute(select_query, (current_time,))
        rows = cursor.fetchall()

        refreshed_events = []

        for event_name, event_time, guild_id, refresh_minutes in rows:
            new_event_time = event_time + timedelta(minutes=refresh_minutes)

            update_query = """
                UPDATE scheduled_events
                SET event_time = %s
                WHERE event_name = %s AND guild_id = %s AND event_time = %s;
            """
            cursor.execute(update_query, (new_event_time, event_name, guild_id, event_time))

            refreshed_events.append({
                "event_name": event_name,
                "event_time": event_time,
                "guild_id": guild_id,
                "refresh_time_in_minutes": refresh_minutes
            })

        connection.commit()
        return refreshed_events

    finally:
        cursor.close()
        connection.close()
