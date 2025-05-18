-- Add any guilds to this as its used as a list of all guilds using this bot
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'getAllGuilds')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'example')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'randomJammyPin')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'randomJammyReact')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'set_bot_identity')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

-- Insert any guilds that would like to use the test function
INSERT INTO guild_enabled_functions_by_guild (guilds, function_name)
VALUES ('896438391040770068,846475513983926273', 'bean_bag')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);