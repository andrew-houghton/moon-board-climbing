from moon.models.base_model import BaseModel
from moon.types.climbset import Climbset
from typing import Union, List
import moon.utils.load_data as load_data
import numpy as np
from sklearn.model_selection import train_test_split
from autokeras.utils import pickle_from_file
from autokeras.preprocessor import OneHotEncoder
from timeit import default_timer as timer
import os


if __name__ == '__main__':
    data = load_data.numpy()
    x_train, x_test, y_train, y_test = train_test_split(
        np.reshape(data['climbs'], (len(data['climbs']), 18*18)).astype(int),
        data['grades'],
        test_size=0.2,
        random_state=42
    )

class Model(BaseModel):
    def sample(self):
        data = load_data.numpy()
        x_train, x_test, y_train, y_test = train_test_split(
            np.reshape(data['climbs'], (len(data['climbs']), 18*18, 1)).astype(int),
            data['grades'],
            test_size=0.2,
            random_state=42
        )

        scriptpath = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(scriptpath, 'imageClassifier.model')
        model = pickle_from_file(model_path)

        start = timer()
        scores = model.predict(x_test)
        print(f"Scored {len(x_test)} climbs in {timer() - start}s")

        return (list(y_test), list(scores))
        

if __name__=="__main__":
    Model().parse()
