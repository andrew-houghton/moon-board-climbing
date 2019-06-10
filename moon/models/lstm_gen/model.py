import os
import pickle

from moon.models.base_model import GeneratorModel
from moon.models.lstm_gen.char_rnn.sample import get_sample
from moon.models.lstm_gen.char_rnn.train import build_model
from moon.models.lstm_gen.prep import prep_no_grade
from moon.types import climb, climbset
from moon.utils.load_data import local_file_path


def clean_sample(sample):
    split_sample = sample.split(climbset.Climbset.get_terminator())

    # Clean up items at the end
    if len(split_sample[0]) <= 1:
        # remove first item if it is too short to be a climb
        split_sample.pop(0)
    split_sample.pop(len(split_sample) - 1)

    return [climb_str for climb_str in split_sample if climb.Climb.valid_input_sample(climb_str)]


class Model(GeneratorModel):
    def name(self):
        return "LSTM"

    def train(self):
        model_dir = os.path.dirname(os.path.realpath(__file__))
        prep_no_grade()
        build_model(model_dir)

    def sample(self):
        model_dir = os.path.dirname(os.path.realpath(__file__))
        num_samples = 1000
        sample_length = 20000
        text_sample = get_sample(model_dir, sample_length, "A")

        generated_climbs = climbset.Climbset(clean_sample(text_sample), "sample")

        print(f"Generated {len(generated_climbs.climbs)} and kept {num_samples}.")
        generated_climbs.climbs = generated_climbs.climbs[:num_samples]

        pickle.dump(generated_climbs, open(local_file_path(__file__, "sample.pickle"), "wb"))
        print("saved sample")

    def load_sample(self):
        return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()
