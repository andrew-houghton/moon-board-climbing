import os
import training_utils.climb_loader as climb_loader
import pickle
import numpy


base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
image_folder = str(base_directory) + '/data/numpy/'


def main():
    # This function loads all the climbs and saves them all as images.
    base_climbset = climb_loader.load_all_as_climbset()

    # The 'counter' variable is only used to log progress
    climbs = []

    for counter, climb in enumerate(base_climbset.climbs):
        # Get climb in image format and save the image to file.
        # climb.as_image().save(image_folder + str(counter) + '.png')
        climbs.append(numpy.asarray(climb.as_image()))

        # Log progress every 50 climbs
        if counter % 100 == 0:
            print('Created {} numpy arrays.'.format(counter))

    return climbs


if __name__ == '__main__':
    climbs = main()

    # Create images folder if it does not exist
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    with open(image_folder+'numpy.pkl', 'wb') as handle:
        pickle.dump(climbs, handle)

    print("Saved climbs")