import load_json_climbs
from pathlib import Path


def create_lstm_strings():
    base_climbset = load_json_climbs.load_all_as_climbset()

    string_save_directory = str(Path().resolve().parent) + '/data/strings/'

    with open(str(string_save_directory) + 'allclimbs_pregrade.txt', 'w') as handle:
        handle.write(base_climbset.pre_grade_string())

    with open(str(string_save_directory) + 'allclimbs_postgrade.txt', 'w') as handle:
        handle.write(base_climbset.post_grade_string())

    with open(str(string_save_directory) + 'allclimbs_nograde.txt', 'w') as handle:
        handle.write(base_climbset.no_grade_string())

if __name__ == '__main__':
    create_lstm_strings()
