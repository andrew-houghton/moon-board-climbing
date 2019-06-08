import pickle

from sklearn.ensemble import RandomForestClassifier

from moon.models.base_model import GradingModel
from moon.utils.load_data import local_file_path


class Model(GradingModel):
    def name(self):
        return "Random Forest"

    def train(self, x_train, x_test, y_train, y_test):
        self.model = RandomForestClassifier(
            n_estimators=10, max_depth=200, random_state=0
        )
        print("Training")
        self.model.fit(x_train, y_train)
        print("Finished training")

    def sample(self, x):
        return self.model.predict(x)

if __name__ == "__main__":
    Model().parse()
