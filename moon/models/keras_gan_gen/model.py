import os
import pickle

from moon.models.base_model import GeneratorModel
from moon.models.keras_gan_gen.gan import GAN
from moon.utils.load_data import local_file_path


class Model(GeneratorModel):
    def name(self):
        return "Keras GAN"

    def train(self):
        climbs, _ = self.preprocess()

        discriminator_path = local_file_path(__file__, "discriminator.h5")
        generator_path = local_file_path(__file__, "generator.h5")

        gan = GAN(climbs, discriminator_path, generator_path, node_scale_factor=8)

        gan.train(epochs=5000, batch_size=32, sample_interval=200)

    def sample(self):
        climbs, _ = self.preprocess()
        discriminator_path = local_file_path(__file__, "discriminator.h5")
        generator_path = local_file_path(__file__, "generator.h5")
        gan = GAN(climbs, discriminator_path, generator_path, node_scale_factor=8)
        gan.load_models()
        images = gan.sample_image()
        print(images)

    def load_sample(self):
        return pickle.load(open(local_file_path(__file__, "sample.pickle"), "rb"))


if __name__ == "__main__":
    Model().parse()
