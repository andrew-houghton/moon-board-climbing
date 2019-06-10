import os

import numpy as np
from keras.layers import LSTM, Dense
from keras.models import Sequential, load_model

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"


class Model:
    def name(self):
        return "Keras LSTM"

    def train(self, x_train, y_train):
        num_classes = y_train.shape[1]
        num_climbs = x_train.shape[0]

        self.model = Sequential()
        self.model.add(LSTM(100, input_shape=(12, 2), dropout=0.2, recurrent_dropout=0.2))
        self.model.add(Dense(num_classes, activation="softmax"))
        self.model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
        self.model.fit(x_train, y_train, epochs=50, batch_size=num_climbs, verbose=0)

    def sample(self, x):
        y_pred = self.model.predict(x)
        bool_preds = [[1 if i == max(row) else 0 for i in row] for row in y_pred]
        return np.asarray(bool_preds)
