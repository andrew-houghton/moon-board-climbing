import pickle

from keras.layers import Dense
from keras.models import Sequential, load_model
from keras.utils import to_categorical
from moon.models.base_model import GradingModel
from moon.utils.load_data import local_file_path


class Model(GradingModel):
    def train(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = Sequential()
        model.add(Dense(20, input_dim=18 * 18, activation="relu"))
        model.add(Dense(15, activation="softmax"))

        model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])

        model.fit(x_train, to_categorical(y_train), epochs=10, batch_size=10)

        model.save(local_file_path(__file__, "model.h5"))
        print("Saved trained model.")

        self.sample()

    def sample(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = load_model(local_file_path(__file__, "model.h5"))

        sample = model.predict(x_test)

        pickle.dump((x_test, y_test, sample), open(local_file_path(__file__, "sample.pickle"), "wb"))
        print("Saved model sample.")

    def load_sample(self):
        return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()
