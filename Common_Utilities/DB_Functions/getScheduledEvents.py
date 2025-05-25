import mysql.connector
from typing import List, Dict, Any
from datetime import datetime, timedelta, time
from Common_Utilities import getDBCursor 

def get_next_aligned_time(current: datetime, interval_minutes: int) -> datetime:
    """Finds the next future time aligned with the interval (in minutes)."""
    total_minutes = current.hour * 60 + current.minute
    remainder = total_minutes % interval_minutes
    minutes_to_add = interval_minutes - remainder if remainder != 0 else 0
    aligned_time = current + timedelta(minutes=minutes_to_add)
    return aligned_time.replace(second=0, microsecond=0)

def getScheduledEvents() -> List[Dict[str, Any]]:
    """
    Retrieves and refreshes scheduled events where event_time <= now.
    Only updates event_time for those exact rows.

    Returns:
        List[Dict[str, Any]]: A list of the original events before refresh.
    """
    connection, cursor = getDBCursor()
    current_time = datetime.utcnow()
    print("testing event updater")

    try:
        select_query = """
            SELECT event_name, event_time, guild_id, refresh_time_in_minutes, config
            FROM scheduled_events
            WHERE event_time <= %s;
        """
        cursor.execute(select_query, (current_time,))
        rows = cursor.fetchall()

        refreshed_events = []

        for event_name, event_time, guild_id, refresh_minutes, config in rows:
            print(f"{event_name} {event_time}")

            if refresh_minutes == 1440:
                # For daily: keep original event time, shift date to tomorrow
                current_utc_date = datetime.utcnow().date() + timedelta(days=1)
                new_event_time = datetime.combine(
                    current_utc_date,
                    time(
                        hour=event_time.hour,
                        minute=event_time.minute,
                        second=event_time.second
                    )
                )
            else:
                # Align to next time slot divisible by the interval
                aligned_dt = get_next_aligned_time(event_time, refresh_minutes)
                new_event_time = aligned_dt


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
                "refresh_time_in_minutes": refresh_minutes,
                "config": config 
            })

        connection.commit()
        return refreshed_events

    finally:
        cursor.close()
        connection.close()
