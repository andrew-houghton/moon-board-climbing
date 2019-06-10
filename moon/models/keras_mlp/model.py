import os

import numpy as np
from keras.layers import Dense
from keras.models import Sequential

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


class Model:
    def name(self):
        return "Keras MLP"

    def train(self, x_train, y_train):
        num_classes = y_train.shape[1]

        self.model = Sequential()
        self.model.add(Dense(20, input_dim=x_train.shape[1], activation="relu"))
        self.model.add(Dense(num_classes, activation="softmax"))
        self.model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
        self.model.fit(x_train, y_train, epochs=10, batch_size=10, verbose=0)

    def sample(self, x):
        y_pred = self.model.predict(x)
        bool_preds = [[1 if i == max(row) else 0 for i in row] for row in y_pred]
        return np.asarray(bool_preds)
