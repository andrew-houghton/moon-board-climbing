# Create your first MLP in Keras
from moon.utils.load_data import load_numpy
import numpy as np
from keras.layers import Dense, Dropout
from keras.models import Sequential, load_model
from keras.regularizers import l1
from keras.utils import to_categorical
from moon.analytics.metrics import expected_diff
from moon.models.base_model import BaseModel
from sklearn.metrics import accuracy_score, auc, confusion_matrix, mean_squared_error
from sklearn.model_selection import train_test_split

np.random.seed(0)


class Model(BaseModel):
    def split_data(self):
        climbs, grades = load_numpy()
        return train_test_split(
            np.reshape(climbs, (len(climbs), 18 * 18)).astype(int),
            grades,
            test_size=0.2,
            random_state=42,
        )

    def train(self):
        x_train, x_test, y_train, y_test = self.split_data()

        model = Sequential()
        model.add(Dense(20, input_dim=18 * 18, activation="relu"))
        model.add(Dense(15, activation="softmax"))

        # Compile model
        model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
        # Fit the model
        model.fit(x_train, to_categorical(y_train), epochs=8, batch_size=10)

        model.save("model.h5")

        self.evaluate()

    def evaluate(self):
        x_train, x_test, y_train, y_test = self.split_data()

        model = load_model("model.h5")

        # evaluate the model
        values = model.predict(x_test)

        predictions = np.argmax(values, axis=1)

        expected_diff(y_test, predictions)
        print(mean_squared_error(y_test, predictions))
        print(confusion_matrix(y_test, predictions))

        scores = model.evaluate(x_test, to_categorical(y_test))
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    def sample(self):
        pass


if __name__ == "__main__":
    Model().parse()
