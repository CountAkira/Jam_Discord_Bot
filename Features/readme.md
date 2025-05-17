Each file needs to go into a folder and contains one command per file. Any commands that you want to show as slash commands need to have a prefix of register_. You can see the example file here on how to set it up.

C:\Users\Akira\Desktop\Jam Chan\Jam 2.0\Features\Example_Feature\example.py

--------------------------------------------------------------------------------------------------------------
You will also need to add this function to the following sql file along with the guilds you want to add this functionality to. This acts as a feature toggle for your server. So if you want only some of the functionality you can do that. Any functionality should be added with the idea that it will be off by default until added. 

C:\Users\Akira\Desktop\Jam Chan\Jam 2.0\DB_Scripts\Repo\Data\001_Guild_Enabled_Functions_Data.sql

Make sure to change the function name to whatever function you are adding so that it can be loaded from this function below. 

from Common_Utilities import getGuildListForFunction

def register_example_command(tree: app_commands.CommandTree, mycursor):
    @tree.command(
        name="example",
        description="My first application Command",
        guilds=getGuildListForFunction(mycursor, "example")
    )
    async def example(interaction: discord.Interaction):
        await interaction.response.send_message("Helloooo!")
        
--------------------------------------------------------------------------------------------------------------
Put any functions associated with these commands into a functions utilities folder

For example say you have a function that sends a message in a particular format but have two commands related to that, say you want to get information for an actor or a movie. You could have a command for each and then in the function

