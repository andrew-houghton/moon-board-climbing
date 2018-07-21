import load_json_climbs
from pathlib import Path

# This function loads all the climbs and saves them all as images.

base_climbset = load_json_climbs.load_all_as_climbset()
script_parent_directory = Path().resolve().parent
image_folder = str(script_parent_directory) + '/data/images/'

# The 'counter' variable is only used to log progress

for counter, climb in enumerate(base_climbset.climbs):
	# Get climb in image format and save the image to file.
    climb.as_image().save(image_folder + str(counter) + '.png')

    # Log progress every 50 climbs
    if counter % 50 == 0:
        print('Created {} images.'.format(counter))
