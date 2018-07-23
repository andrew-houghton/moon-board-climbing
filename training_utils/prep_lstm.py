import os
from . import climb_loader
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    # Get all the climbs
    all_climbs = climb_loader.load_all_as_climbset()

    # Save them in different formats
    data_directory = base_directory + '/data/lstm_files/'
    save_data = [
        ['post_grade', all_climbs.post_grade_string()],
        ['no_grade', all_climbs.no_grade_string()],
        ['pre_grade', all_climbs.pre_grade_string()],
    ]

    # File writing
    for data in save_data:
        folder_name, climb_text = data
        write_path = data_directory + folder_name
        os.makedirs(write_path)
        with open(write_path + '/input.txt', 'w') as handle:
            handle.write(climb_text)


if __name__ == '__main__':
    main()
