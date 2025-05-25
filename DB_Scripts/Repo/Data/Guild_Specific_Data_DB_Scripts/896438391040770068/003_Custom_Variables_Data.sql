-- Emotes that jammy can use to react with in jams
INSERT INTO custom_variables (guild_id, var_name, var_value)
VALUES (
    896438391040770068,
    'customReactEmotes',
    JSON_ARRAY(
        '<:valle:900498352263807018>',
        '<:OmegaFlushed:904878039777820702>',
        '<:jomLife:925236021187182592>',
        '<:ayaya:898723357678264350>',
        '<:pog:898722897407909959>',
        '<:jomseph:898722577554497568>'
    )
)
ON DUPLICATE KEY UPDATE
    var_value = VALUES(var_value);

-- Fumo daily upload configuration
INSERT INTO custom_variables (guild_id, var_name, var_value)
VALUES (
    896438391040770068,
    'fumoDailyChannel',
    JSON_OBJECT(
        'channel', '896438391766413385',
        'emote', '<a:cirBoogie:1376073733449711686>'
    )
)
ON DUPLICATE KEY UPDATE
    var_value = VALUES(var_value);
