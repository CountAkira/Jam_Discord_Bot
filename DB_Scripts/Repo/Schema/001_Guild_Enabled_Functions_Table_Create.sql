CREATE TABLE IF NOT EXISTS guild_enabled_functions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    guilds TEXT NOT NULL,
    function_name VARCHAR(255) NOT NULL,
    UNIQUE KEY unique_function_name (function_name)
);