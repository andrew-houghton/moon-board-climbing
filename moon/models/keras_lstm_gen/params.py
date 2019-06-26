from dataclasses import dataclass
from typing import List
from keras.optimizers import RMSprop


@dataclass
class default:
    max_climb_length: int = 12
    epochs: Int = 50
    num_lstm_cells: List[int] = [128]
    optimizer: Any = RMSprop(lr=0.01)
    text_diversity: float = 0.8
    batch_size: int = 128


@dataclass
class parameter_space:
    epochs: List[int] = [50]
    max_climb_length: List[int] = [8, 12, 16, 20]
    num_lstm_cells: List[List[int]] = [[128]]
    optimizer: List[Any] = [RMSprop(lr=0.01)]
    text_diversity: List[float] = [0.2, 0.5, 1.0, 1.2]
