import load_json_climbs
from pathlib import Path

base_climbset = load_json_climbs.load_all_as_climbset()

for counter, climb in enumerate(base_climbset.climbs):
    script_parent_directory = Path().resolve().parent
    image_folder = str(script_parent_directory) + '/data/images/'
    climb.as_image().save(image_folder + str(counter) + '.png')
    if counter % 50 == 0:
        print('Created {} images.'.format(counter))
