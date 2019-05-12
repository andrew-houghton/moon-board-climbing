# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.regularizers import l1
from keras.utils import to_categorical
from moon.models.base_model import BaseModel
from sklearn.model_selection import train_test_split
import moon.utils.load_data as load_data
import numpy as np
from sklearn.metrics import auc, accuracy_score, confusion_matrix, mean_squared_error


np.random.seed(0)

def expected_diff(test_data, score_data):
    ex_sum_diff=sum([abs(test_data[i]-score_data[i]) for i in range(len(test_data))])
    print(f"Expected difference from correct grade: {ex_sum_diff/len(test_data)}")

class Model(BaseModel):
    def split_data(self):
        data = load_data.numpy()
        return train_test_split(
            np.reshape(data['climbs'], (len(data['climbs']), 18*18)).astype(int),
            data['grades'],
            test_size=0.2,
            random_state=42
        )

    def train(self):
        x_train, x_test, y_train, y_test = self.split_data()

        model = Sequential()
        model.add(Dense(100, input_dim=18*18, activation='relu'))
        model.add(Dense(15, activation='softmax'))

        # Compile model
        model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
        # Fit the model
        model.fit(x_train, to_categorical(y_train), epochs=8, batch_size=10)
        # evaluate the model
        values = model.predict(x_test)
        
        predictions = np.argmax(values, axis=1)

        expected_diff(y_test, predictions)
        print(mean_squared_error(y_test, predictions))
        print(confusion_matrix(y_test, predictions))
        
        scores = model.evaluate(x_test, to_categorical(y_test))
        print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    def sample(self):
        pass

if __name__=="__main__":
    Model().parse()
