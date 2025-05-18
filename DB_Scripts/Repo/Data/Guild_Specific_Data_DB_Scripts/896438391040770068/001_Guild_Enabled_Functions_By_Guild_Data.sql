-- Insert guilds using 'example' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('example', '896438391040770068', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;

-- Insert guilds using 'randomJammyPin' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('randomJammyPin', '896438391040770068', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;

-- Insert guilds using 'randomJammyReact' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('randomJammyReact', '896438391040770068', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;

-- Insert guilds using 'set_bot_identity' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('set_bot_identity', '896438391040770068', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;

-- Insert guilds using 'bean_bag' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('bean_bag', '896438391040770068', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;
