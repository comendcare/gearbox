import json

def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

config = load_config("config/global_config.json")

