from dataclasses import dataclass
from typing import Any, Tuple
from keras.optimizers import RMSprop
from moon.models import keras_lstm_gen
from moon.utils.load_data import load_climbset, local_file_path
import itertools
from pprint import pprint
from functools import partial
import time


@dataclass
class Parameters:
    epochs: int = 200
    max_climb_length: int = 16
    num_lstm_cells: Tuple[int] = (64,)
    optimizer: Any = RMSprop(lr=0.01)
    batch_size: int = 512


@dataclass
class ParameterSpace:
    epochs: Tuple[int] = (15,)
    max_climb_length: Tuple[int] = (16,)
    num_lstm_cells: Tuple[Tuple[int]] = ((256,), (128,), (64,), (32,))
    optimizer: Tuple[Any] = (RMSprop(lr=0.01),)
    batch_size: Tuple[int] = (1024,)

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
    print(f"Training {parameters}")
    start = time.time()
    lstm = keras_lstm_gen.Model()
    history = lstm.train(climbset, parameters)
    print(f"Training {parameters} took {time.time()-start}")
    return (
        parameters,
        min(history.history["loss"]),
        min(history.history["val_loss"]),
        time.time() - start,
    )


def search():
    parameter_args = ParameterSpace().product()
    hyper_parameter_combinations = [Parameters(*args) for args in parameter_args]

    print(f"Generated {len(hyper_parameter_combinations)} sets of parameters")
    train_func = partial(train_model, climbset=load_climbset("2016"))
    results = list(map(train_func, hyper_parameter_combinations))
    pprint(results)


if __name__ == "__main__":
    search()
