from keras.layers import LSTM, Dense
from keras.models import Sequential, load_model


class Model:
    def name(self):
        return "Keras LSTM"

    def train(self, x_train, y_train):
        self.model = Sequential()
        self.model.add(
            LSTM(100, input_shape=(12, 2), dropout=0.2, recurrent_dropout=0.2)
        )
        self.model.add(Dense(15, activation="softmax"))
        self.model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
        self.model.fit(x_train, y_train, epochs=50, batch_size=13570)

    def sample(self, x):
        return self.model.predict(x)
