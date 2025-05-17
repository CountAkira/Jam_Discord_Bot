# Setup

Current Installed Versions 
python: 3.12.1
discord.py: 2.5.2
mysql-connector-python: 8.3.0

Follow setup instructions for discord.py and make sure you have python installed. 
https://discordpy.readthedocs.io/en/stable/intro.html

Install mysql python connector
python -m pip install mysql-connector-python

You will need to go here and set up a bot and get your token https://discord.com/developers/docs/quick-start/getting-started

Add your config information to Config\config_example.txt and rename the file to config.json. 

Add your guild id in the values section with a preceding comma to any functions you want and the getAllGuilds function to the following file.
C:\Users\Akira\Desktop\Jam Chan\Jam 2.0\DB_Scripts\Repo\Data\001_Guild_Enabled_Functions_Data.sql

Run the bot by doing py jam.py in the top directory