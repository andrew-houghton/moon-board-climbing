from dataclasses import dataclass
from typing import Any, Tuple
from keras.optimizers import RMSprop
from moon.models import keras_lstm_gen
from moon.utils.load_data import load_climbset, local_file_path


@dataclass
class default:
    max_climb_length: int = 12
    epochs: int = 2
    num_lstm_cells: Tuple[int] = (128,)
    optimizer: Any = RMSprop(lr=0.01)
    batch_size: int = 128


@dataclass
class parameter_space:
    epochs: Tuple[int] = (10,)
    max_climb_length: Tuple[int] = (12,)
    num_lstm_cells: Tuple[Tuple[int]] = ([128],)
    optimizer: Tuple[Any] = (RMSprop(lr=0.01),)
    text_diversity: Tuple[float] = (1.0,)


def search():
    climbset = load_climbset(year)
    lstm = keras_lstm_gen.Model()
    parameter_space = arameter_space()


def main(year):
    num_climbs = 500

    # Load climbset

    # Sample generators
    sample = lstm.sample(climbset, num_climbs, sampling_parameters)

    # Save to file
    file_data = {"original": climbset, "lstm": sample}

    print(f"Saving {len(file_data)} climbsets")
    pickle.dump(
        file_data, open(local_file_path(__file__, f"{year}.pickle"), "wb")
    )


if __name__ == "__main__":
    main("2016")
    main("2017")
