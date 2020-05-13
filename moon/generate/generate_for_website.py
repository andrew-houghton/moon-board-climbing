import pickle

from moon.models import keras_lstm_gen
import moon.models.keras_lstm_gen.params as params
from moon.utils.load_data import load_climbset, local_file_path


def main(year):
    num_climbs = 500

    # Load climbset
    climbset = load_climbset(year)

    # Sample generators
    lstm = keras_lstm_gen.Model()
    sampling_parameters = params.Parameters()
    sample = lstm.sample(climbset, num_climbs, sampling_parameters)

    # Save to file
    file_data = {"original": climbset, "lstm": sample}

    print(f"Saving {len(file_data)} climbsets")
    pickle.dump(file_data, open(local_file_path(__file__, f"{year}.pickle"), "wb"))


if __name__ == "__main__":
    main("2016")
    main("2017")
