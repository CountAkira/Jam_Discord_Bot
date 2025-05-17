-- Add any guilds to this as its used as a list of all guilds using this bot
INSERT INTO guild_enabled_functions (guilds, function_name)
VALUES ('846475513983926273,896438391040770068', 'getAllGuilds')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions (guilds, function_name)
VALUES ('846475513983926273,896438391040770068', 'example')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);