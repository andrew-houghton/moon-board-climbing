import json
from pathlib import Path

script_parent_directory = Path().resolve().parent
with open(str(script_parent_directory)+'/data/json/all.json') as handle:
	loaded_data = json.load(handle)
	
