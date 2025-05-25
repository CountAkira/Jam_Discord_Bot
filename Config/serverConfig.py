import json

# Load the config once when the module is imported
with open('Config/serverConfig.json', 'r') as file:
    serverConfig = json.load(file)