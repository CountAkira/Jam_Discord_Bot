-- fumoDaily event to post a fumo video daily in general in jams
INSERT INTO scheduled_events (event_name, event_time, guild_id, refresh_time_in_minutes, config)
VALUES ('fumoDaily', '2025-05-16 16:00:00', 896438391040770068, 1440, '{"post_channel_id": "896438391766413385"}')
ON DUPLICATE KEY UPDATE
  -- event_time = VALUES(event_time),
  refresh_time_in_minutes = VALUES(refresh_time_in_minutes),
  config = VALUES(config);

-- test scheduler event, if you dont want to update the time every bot restart then leave out the event time value change, otherwise leave it commented
INSERT INTO scheduled_events (event_name, event_time, guild_id, refresh_time_in_minutes, config)
VALUES ('test6', '2025-05-22 00:00:00', 896438391040770068, 30, '{"post_channel_id": "896438391766413385"}')
ON DUPLICATE KEY UPDATE
  -- event_time = VALUES(event_time),
  refresh_time_in_minutes = VALUES(refresh_time_in_minutes),
  config = VALUES(config);