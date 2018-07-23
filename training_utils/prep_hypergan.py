import os
from . import climb_loader
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_folder = str(base_directory) + '/data/images/'


def main():
    # This function loads all the climbs and saves them all as images.
    base_climbset = climb_loader.load_all_as_climbset()

    # Create images folder if it does not exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # The 'counter' variable is only used to log progress

    for counter, climb in enumerate(base_climbset.climbs):
        # Get climb in image format and save the image to file.
        climb.as_image().save(image_folder + str(counter) + '.png')

        # Log progress every 50 climbs
        if counter % 100 == 0:
            print('Created {} images.'.format(counter))

if __name__ == '__main__':
    main()
