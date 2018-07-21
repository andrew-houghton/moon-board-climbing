import load_json_climbs
from pathlib import Path

# This creates a climbset and saves it in various formats ready for the LSTM to train on.

def create_lstm_strings():
    base_climbset = load_json_climbs.load_all_as_climbset()

    string_save_directory = str(Path().resolve().parent) + '/data/lstm_files/'

    with open(str(string_save_directory) + 'pre_grade/' + 'input.txt', 'w') as handle:
        handle.write(base_climbset.pre_grade_string())

    with open(str(string_save_directory) + 'post_grade/' + 'input.txt', 'w') as handle:
        handle.write(base_climbset.post_grade_string())

    with open(str(string_save_directory) + 'no_grade/' + 'input.txt', 'w') as handle:
        handle.write(base_climbset.no_grade_string())

if __name__ == '__main__':
    create_lstm_strings()
