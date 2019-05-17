import os
import pickle
from moon.models.base_model import GeneratorModel
from moon.utils.load_data import local_file_path
from moon.models.keras_gan_gen.gan import GAN


class Model(GeneratorModel):
    def train(self):
        climbs, _ = self.preprocess()
        gan = GAN(climbs)
        gan.train(epochs=1000, batch_size=32, sample_interval=50)

    def sample(self):
        # model_dir = os.path.dirname(os.path.realpath(__file__))
        # pickle.dump(generated_climbs, open(local_file_path(__file__, "sample.pickle"), "wb"))
        # print("saved sample")
        pass

    def load_sample(self):
        return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()
