CREATE TABLE IF NOT EXISTS guild_enabled_functions (
    function_name VARCHAR(255) NOT NULL,
    guilds TEXT NOT NULL,

    PRIMARY KEY (function_name)
);
