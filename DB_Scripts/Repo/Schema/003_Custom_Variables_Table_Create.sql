CREATE TABLE IF NOT EXISTS custom_variables (
    guild_id BIGINT NOT NULL,
    var_name VARCHAR(255) NOT NULL,
    var_value JSON NOT NULL,

    PRIMARY KEY (guild_id, var_name)
);
