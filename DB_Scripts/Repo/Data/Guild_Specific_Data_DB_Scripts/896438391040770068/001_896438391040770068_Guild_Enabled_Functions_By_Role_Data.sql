-- Add any roles along with the function you want those roles authorized for, if roles an empty string or entry it will auth for all users assuming its enabled
-- You can use the role id or the name for the roles, just know its case sensitive and will strip out any spaces when looking if role is authorized

-- Adds set bot identity authorization only for king kaiju role
INSERT INTO guild_enabled_functions_by_role (guild, function_name, roles)
VALUES ('896438391040770068', 'set_bot_identity', '926774582097084436')
ON DUPLICATE KEY UPDATE
  roles = VALUES(roles);


-- Adds set bot identity authorization only for king kaiju role
INSERT INTO guild_enabled_functions_by_role (guild, function_name, roles)
VALUES ('896438391040770068', 'example', '')
ON DUPLICATE KEY UPDATE
  roles = VALUES(roles);

