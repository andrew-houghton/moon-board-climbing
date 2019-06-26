from dataclasses import dataclass
from typing import Any, Tuple
from keras.optimizers import RMSprop


@dataclass
class default:
    max_climb_length: int = 12
    epochs: int = 10
    num_lstm_cells: Tuple[int] = (128,)
    optimizer: Any = RMSprop(lr=0.01)
    text_diversity: float = 0.8
    batch_size: int = 128


# @dataclass
# class parameter_space:
#     epochs: Tuple[int] = [50]
#     max_climb_length: Tuple[int] = [8, 12, 16, 20]
#     num_lstm_cells: Tuple[Tuple[int]] = [[128]]
#     optimizer: Tuple[Any] = [RMSprop(lr=0.01)]
#     text_diversity: Tuple[float] = [0.2, 0.5, 1.0, 1.2]
