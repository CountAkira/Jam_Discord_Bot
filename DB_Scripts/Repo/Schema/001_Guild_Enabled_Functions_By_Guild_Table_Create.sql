CREATE TABLE IF NOT EXISTS guild_enabled_functions_by_guild (
    function_name VARCHAR(255) NOT NULL,
    guilds TEXT NOT NULL,

    PRIMARY KEY (function_name)
);
