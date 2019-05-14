from moon.models.base_model import GradingModel
import xgboost as xgb
import pickle
from moon.utils.load_data import local_file_path
from moon.models.lstm_gen.prep import prep_no_grade
import moon.models.lstm_gen.char_rnn.train as train

class Model(GradingModel):
    def train(self):
        input_file = prep_no_grade()

        train.build_model(input_file, )

        self.sample()

    # def sample(self):
    #     x_train, x_test, y_train, y_test = self.preprocess()

    #     xgb_model = pickle.load(open(local_file_path(__file__, "model.pickle"), "rb"))
    #     sample = xgb_model.predict(x_test)

    #     pickle.dump((x_test, y_test, sample), open(local_file_path(__file__, "sample.pickle"), "wb"))
    #     print("Saved model sample.")

    # def load_sample(self):
    #     return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()
