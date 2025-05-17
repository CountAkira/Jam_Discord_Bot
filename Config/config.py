import json

# Load the config once when the module is imported
with open('Config/config.json', 'r') as file:
    config = json.load(file)