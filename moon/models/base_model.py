import argparse
from typing import List, Tuple, Union

import moon
from moon.types.climbset import Climbset


class BaseModel:
    def parse(self):
        function_map = {"prep": self.prep, "train": self.train, "sample": self.sample}

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("prep", nargs="?")
        group.add_argument("train", nargs="?")
        group.add_argument("sample", nargs="?")
        args = [i for i in parser.parse_args().__dict__.values()][0]

        function_map[args]()

    def prep(self) -> None:
        pass

    # def train(self, input_range: Tuple[int, int] = (0, 13570)) -> None:
    def train(self) -> None:
        pass


class GeneratorModel(BaseModel):
    # def sample(self, num: int) -> Climbset:
    def sample(self) -> Climbset:
        pass


class GradingModel(BaseModel):
    # def sample(self, climbs: Climbset) -> List[Union[int, float]]:
    def sample(self) -> List[Union[int, float]]:
        pass
