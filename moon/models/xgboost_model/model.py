import pickle

import xgboost as xgb

from moon.models.base_model import GradingModel
from moon.utils.load_data import local_file_path


class Model(GradingModel):
    def name(self):
        return "XGBoost"

    def train(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        xgb_model = xgb.XGBClassifier(
            objective="multi:softprob", random_state=42
        )

        print("Training")
        xgb_model.fit(x_train, y_train)
        pickle.dump(
            xgb_model, open(local_file_path(__file__, "model.pickle"), "wb")
        )

        print("Saved trained model.")

        self.sample()

    def sample(self):
        x_train, x_test, y_train, y_test = self.preprocess()

        xgb_model = pickle.load(
            open(local_file_path(__file__, "model.pickle"), "rb")
        )
        sample = xgb_model.predict(x_test)

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
