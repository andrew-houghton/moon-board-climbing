import pickle
from pprint import pprint

import numpy as np
from keras.layers import LSTM, Dense
from keras.models import Sequential, load_model
from keras.preprocessing import sequence
from keras.utils import to_categorical
from moon.models.base_model import GradingModel
from moon.utils.load_data import load_climbset, local_file_path
from sklearn.model_selection import train_test_split


def hold_list(climb):
    return [(hold.col, hold.row) for hold in climb.holds]


def move_sizes(hold_list):
    hold_queue = [hold_list[0]]

    for i in range(len(hold_list) - 1):
        hold = hold_list[i]
        next_hold = hold_list[i + 1]
        hold_queue.append(tuple(i - j for i, j in zip(next_hold, hold)))
        hold_queue.append(next_hold)
    return hold_queue


class Model(GradingModel):
    self.name = "Keras LSTM"

    def preprocess(self):
        climbset = load_climbset()

        holds = list(map(hold_list, climbset.climbs))
        # holds_and_moves = list(map(move_sizes, holds))

        grades = [i.grade.grade_number for i in climbset.climbs]

        max_climb_length = 12
        holds_pad = sequence.pad_sequences(holds, maxlen=max_climb_length)

        return train_test_split(
            holds_pad, grades, test_size=0.2, random_state=42
        )

    def train(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = Sequential()
        model.add(
            LSTM(100, input_shape=(12, 2), dropout=0.2, recurrent_dropout=0.2)
        )
        model.add(Dense(15, activation="softmax"))

        model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])

        model.fit(
            x_train, to_categorical(y_train), epochs=50, batch_size=13570
        )

        model.save(local_file_path(__file__, "model.h5"))
        print("Saved trained model.")

        self.sample()

    def sample(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = load_model(local_file_path(__file__, "model.h5"))

        sample = model.predict(x_test)

        print(model.metrics_names)
        print(model.evaluate(x_test, to_categorical(y_test)))

        pickle.dump(
            (x_test, y_test, sample),
            open(local_file_path(__file__, "sample.pickle"), "wb"),
        )
        print("Saved model sample.")

    def load_sample(self):
        return pickle.load(
            open(local_file_path(__file__, "sample.pickle"), "rb")
        )


if __name__ == "__main__":
    Model().parse()
