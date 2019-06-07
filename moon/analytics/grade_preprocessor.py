from typing import List

from keras.utils import to_categorical


class BasePreprocessor:
    def preprocess(self, grade: int) -> List[bool]:
        pass


class CategoricalPreprocessor(BasePreprocessor):
    def preprocess(self, grade: int) -> List[bool]:
        return to_categorical(grade)
