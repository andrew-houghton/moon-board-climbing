from typing import List

import numpy as np
from keras.utils import to_categorical


class CategoricalPreprocessor:
    def preprocess(self, grade: int) -> List[bool]:
        return to_categorical(grade)


class HalfGradePreprocessor:
    def preprocess(self, grade: int) -> List[bool]:
        grade = np.floor(grade / 2)
        return to_categorical(grade)


class FlandersPreprocessor:
    def preprocess(self, grade: int) -> int:
        return grade


class SplitPreprocessor:
    def __init__(self, threshold):
        self.threshold = threshold

    def preprocess_item(self, grade: int) -> List[bool]:
        if grade > self.threshold:
            return [True, False]
        else:
            return [False, True]

    def preprocess(self, grade):
        return np.asarray([self.preprocess_item(i) for i in grade])
