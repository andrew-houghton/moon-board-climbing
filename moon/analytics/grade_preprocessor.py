from typing import List

from keras.utils import to_categorical
import numpy as np


class BasePreprocessor:
    def preprocess(self, grade: int) -> List[bool]:
        pass


class CategoricalPreprocessor(BasePreprocessor):
    def preprocess(self, grade: int) -> List[bool]:
        return to_categorical(grade)


class FlandersPreprocessor(BasePreprocessor):
    def preprocess(self, grade: int) -> int:
        return grade


class SplitPreprocessor(BasePreprocessor):
    def __init__(self, threshold):
        self.threshold = threshold

    def preprocess_item(self, grade: int) -> List[bool]:
        if grade > self.threshold:
            return [True, False]
        else:
            return [False, True]

    def preprocess(self, grade):
        return np.asarray([self.preprocess_item(i) for i in grade])
