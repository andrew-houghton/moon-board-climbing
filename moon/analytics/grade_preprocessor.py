from typing import List
from keras.utils import to_categorical


class BasePreprocessor:
    def preprocess(self, grade: Int) -> List[bool]:
        pass

class Preprocessor(BasePreprocessor):
    def preprocess(self, grade: Int) -> List[bool]:
        return to_categorical(grade)
