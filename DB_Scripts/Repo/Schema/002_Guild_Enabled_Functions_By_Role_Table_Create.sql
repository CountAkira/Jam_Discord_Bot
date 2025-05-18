CREATE TABLE IF NOT EXISTS guild_enabled_functions_by_role (
    function_name VARCHAR(255) NOT NULL,
    guild VARCHAR(255) NOT NULL,
    roles TEXT,

    PRIMARY KEY (function_name, guild)
);
