CREATE TABLE IF NOT EXISTS scheduled_events (
    event_name VARCHAR(100) NOT NULL,
    event_time DATETIME NOT NULL,
    guild_id BIGINT NOT NULL,
    refresh_time_in_minutes INT NOT NULL,
    config JSON DEFAULT NULL,

    PRIMARY KEY (event_name, guild_id)
);
