CREATE TABLE IF NOT EXISTS guild_enabled_functions_by_guild (
    function_name VARCHAR(255) NOT NULL,
    guild_id VARCHAR(255) NOT NULL,
    is_enabled BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (function_name, guild_id)
);
