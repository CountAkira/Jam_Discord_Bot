-- Insert guilds using 'example' function
INSERT INTO guild_enabled_functions_by_guild (function_name, guild_id, is_enabled) VALUES
('example', '846475513983926273', TRUE)
ON DUPLICATE KEY UPDATE is_enabled = TRUE;

