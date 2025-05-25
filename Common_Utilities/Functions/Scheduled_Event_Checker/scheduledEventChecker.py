import importlib
from Common_Utilities import getScheduledEvents

EVENTS_PACKAGE = "Common_Utilities.Functions.Scheduled_Event_Checker.Events"
module_cache = {}  # Cache to store loaded modules

# Dynamically grabs all scheduled events and checks the event name for a matching function in the events folder 
async def scheduledEventChecker(bot):
    events = getScheduledEvents()

    for event in events:
        event_name = event["event_name"]
        config = event.get("config", {})
        guild_id = event.get("guild_id", {})

        try:
            # Use cached module if available, else import and cache it
            if event_name in module_cache:
                module = module_cache[event_name]
            else:
                module = importlib.import_module(f"{EVENTS_PACKAGE}.{event_name}")
                module_cache[event_name] = module

            # Try to get the function with the same name as the event
            event_func = getattr(module, event_name)

            # Call the function
            await event_func(bot, config, guild_id)

        except ModuleNotFoundError:
            print(f"[WARN] No module found for event: {event_name}")
        except AttributeError:
            print(f"[WARN] Module '{event_name}' does not have a callable '{event_name}' function")
        except Exception as e:
            print(f"[ERROR] Failed to run event '{event_name}': {e}")
