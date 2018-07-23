# This file loads in the data which was scraped and puts it into one clean json file.

import json
from pathlib import Path

# Find parent directory to access raw data
script_parent_directory = Path().resolve().parent

# Load all unprocessed json data
with open(str(script_parent_directory) + '/data/json/all.json') as handle:
    lines = handle.read().split('\n')

# Data is stored on seperate lines which all contain json objects

# loop through the lines and process each json object
# only save the data which is we will use later

all_climbs = []  # Create an empty array to hold the climbs

for json_line in lines:  # loop through all the different json strings
    json_data = json.loads(json_line)  # change the json string into a python object

    # Go through all the climbs in the json object (a single json string contains multiple climbs)
    for climb_obj in json_data['Data']:
        # Collect all the relevant info for the current climb
        saved_obj = {}

        saved_obj['Grade'] = climb_obj['Grade']
        saved_obj['UserRating'] = climb_obj['UserRating']

        # Keep only the data in momes which is needed
        saved_obj['Moves'] = [move['Description'] for move in climb_obj['Moves']]

        all_climbs.append(saved_obj)

# Write the collected data to a file in json format
with open(str(script_parent_directory) + '/data/json/combined.json', 'w') as handle:
    json.dump(all_climbs, handle)
