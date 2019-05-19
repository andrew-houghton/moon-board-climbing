import argparse
from typing import List, Tuple, Union

import numpy as np
from moon.types.climbset import Climbset
from moon.utils.load_data import load_numpy
from sklearn.model_selection import train_test_split

np.random.seed(0)


class BaseModel:
    def parse(self):
        function_map = {"prep": self.prep, "train": self.train, "sample": self.sample}

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("prep", nargs="?")
        group.add_argument("train", nargs="?")
        group.add_argument("sample", nargs="?")

        args = parser.parse_args()
        args = [i for i in args.__dict__.values() if i][0]

        function_map[args]()

    def prep(self) -> None:
        pass

    def train(self) -> None:
        pass


class GeneratorModel(BaseModel):
    def sample(self) -> Climbset:
        pass

    def preprocess(self):
        return load_numpy()


class GradingModel(BaseModel):
    def sample(self) -> List[Union[int, float]]:
        pass

    def preprocess(self):
        climbs, grades = load_numpy()
        return train_test_split(
            np.reshape(climbs, (len(climbs), 11 * 18)).astype(int), grades, test_size=0.2, random_state=42
        )
