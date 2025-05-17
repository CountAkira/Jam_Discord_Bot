# Repo SQL

All files added to the repo folder will be kept in git and pushed to the repo if you so choose.

# Guide To Making SQL Scripts

- Always use `IF NOT EXISTS` when creating tables, indexes, views, etc.

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE
);

- Avoid inserting the same seed data twice.

INSERT INTO roles (name)
SELECT * FROM (SELECT 'admin') AS tmp
WHERE NOT EXISTS (
    SELECT name FROM roles WHERE name = 'admin'
) LIMIT 1;

- For any scripts that require updates like `001_Guild_Enabled_Functions_Data.sql` make sure to use `ON DUPLICATE KEY UPDATE`. You can also choose to simply make a new script with an update if it is something not updated often. 

INSERT INTO guild_enabled_functions (guilds, function_name)
VALUES ('846475513983926273,896438391040770068', 'example')
ON DUPLICATE KEY UPDATE
  guilds = VALUES(guilds);

- Prefix files numerically to enforce execution order

001_create_users_table.sql
002_create_roles_table.sql
010_seed_default_users.sql

# 001_Guild_Enabled_Functions_Data.sql

Add any functions you would like to have in your server here. Just add your guild to the existing lists.

# 002_Scheduled_Events_Data.sql

Add any scheduled events you would like to have in your server here. You will need to make an individual entry for every event and guild combo. All timestamps are in utc.

# 003_Custom_Variables_Table_Create

Takes in a guild_id and var_name which then outputs a var_value. 