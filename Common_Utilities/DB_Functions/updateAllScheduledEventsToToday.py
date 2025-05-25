import mysql.connector
from datetime import datetime, timedelta, time
from Common_Utilities import getDBCursor

def updateAllScheduledEventsToToday():
    """
    Updates all scheduled events in the database to have today's UTC date
    but preserves the original time (hour/min/sec) from each event.
    """
    connection, cursor = getDBCursor()
    current_utc_date = datetime.utcnow().date()

    try:
        select_query = """
            SELECT event_name, event_time, guild_id, refresh_time_in_minutes
            FROM scheduled_events;
        """
        cursor.execute(select_query)
        rows = cursor.fetchall()

        for event_name, event_time, guild_id, refresh_time_in_minutes in rows:

            # if event is daily then don't update it, that will automatically happen in the scheduled event getter
            if refresh_time_in_minutes != 1440:
                # Combine today's date with the original time of the event
                new_event_time = datetime.combine(
                    current_utc_date,
                    time(
                        hour=event_time.hour,
                        minute=event_time.minute,
                        second=event_time.second
                    )
                )

                update_query = """
                    UPDATE scheduled_events
                    SET event_time = %s
                    WHERE event_name = %s AND guild_id = %s;
                """
                cursor.execute(update_query, (new_event_time, event_name, guild_id))

        connection.commit()
        print("All scheduled events have been updated to today's date with their original times.")

    finally:
        cursor.close()
        connection.close()

# Run the function
if __name__ == "__main__":
    updateAllScheduledEventsToToday()
