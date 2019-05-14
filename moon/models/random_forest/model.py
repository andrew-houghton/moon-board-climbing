from moon.models.base_model import GradingModel
from sklearn.ensemble import RandomForestClassifier
import pickle
from moon.utils.load_data import local_file_path


class Model(GradingModel):
    def train(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = RandomForestClassifier(n_estimators=100, max_depth=200, random_state=0)
        print("Training")

        model.fit(x_train, y_train)
        pickle.dump(model, open(local_file_path(__file__, "model.pickle"), "wb"))

        print("Saved trained model.")

        self.sample()

    def sample(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        model = pickle.load(open(local_file_path(__file__, "model.pickle"), "rb"))
        sample = model.predict(x_test)

        pickle.dump((x_test, y_test, sample), open(local_file_path(__file__, "sample.pickle"), "wb"))
        print("Saved model sample.")

    def load_sample(self):
        return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()