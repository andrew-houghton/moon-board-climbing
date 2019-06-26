from dataclasses import dataclass
from typing import Any, Tuple
from keras.optimizers import RMSprop
from moon.models import keras_lstm_gen
from moon.utils.load_data import load_climbset, local_file_path
import itertools
from pprint import pprint
from functools import partial


@dataclass
class Parameters:
    epochs: int = 2
    max_climb_length: int = 12
    num_lstm_cells: Tuple[int] = (128,)
    optimizer: Any = RMSprop(lr=0.01)
    batch_size: int = 128


@dataclass
class ParameterSpace:
    epochs: Tuple[int] = (2,)
    max_climb_length: Tuple[int] = (12,)
    num_lstm_cells: Tuple[Tuple[int]] = ([128], [32])
    optimizer: Tuple[Any] = (RMSprop(lr=0.01),)
    batch_size: Tuple[int] = (128,)

    def product(self):
        return list(
            itertools.product(
                self.epochs,
                self.max_climb_length,
                self.num_lstm_cells,
                self.optimizer,
                self.batch_size,
            )
        )


def train_model(parameters, climbset):
    lstm = keras_lstm_gen.Model()
    history = lstm.train(climbset, parameters)
    return parameters, history.history


def search():
    parameter_args = ParameterSpace().product()
    hyper_parameter_combinations = [
        Parameters(*args) for args in parameter_args
    ]

    train_func = partial(train_model, climbset=load_climbset("2016"))
    results = list(map(train_func, hyper_parameter_combinations))
    pprint(results)


if __name__ == "__main__":
    search()
