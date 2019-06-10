from __future__ import division, print_function

import sys

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Activation, BatchNormalization, Dense, Flatten, Input, Reshape
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Model, Sequential, load_model
from keras.optimizers import Adam

from moon.utils.load_data import local_file_path

matplotlib.use("TkAgg")


class GAN:
    def __init__(self, input_data, discriminator_path, generator_path, node_scale_factor=64):
        self.input_data = input_data
        self.discriminator_path = discriminator_path
        self.generator_path = generator_path
        self.node_scale_factor = node_scale_factor
        self.channels = 1
        self.img_shape = (self.input_data.shape[1], self.input_data.shape[2], self.channels)
        self.latent_dim = 100

        # Build and compile the discriminator
        self.discriminator = self.build_discriminator()
        self.discriminator.compile(
            loss="binary_crossentropy", optimizer=Adam(0.0002, 0.5), metrics=["accuracy"]
        )

        # Build the generator
        self.generator = self.build_generator()

        # The generator takes noise as input and generates imgs
        z = Input(shape=(self.latent_dim,))
        img = self.generator(z)

        # For the combined model we will only train the generator
        self.discriminator.trainable = False

        # The discriminator takes generated images as input and determines validity
        validity = self.discriminator(img)

        # The combined model  (stacked generator and discriminator)
        # Trains the generator to fool the discriminator
        self.combined = Model(z, validity)
        self.combined.compile(loss="binary_crossentropy", optimizer=Adam(0.0002, 0.5))

    def build_generator(self):

        model = Sequential()

        model.add(Dense(self.node_scale_factor, input_dim=self.latent_dim))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(self.node_scale_factor * 2))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(self.node_scale_factor * 4))
        model.add(LeakyReLU(alpha=0.2))
        model.add(BatchNormalization(momentum=0.8))
        model.add(Dense(np.prod(self.img_shape), activation="tanh"))
        model.add(Reshape(self.img_shape))

        model.summary()

        noise = Input(shape=(self.latent_dim,))
        img = model(noise)

        return Model(noise, img)

    def build_discriminator(self):

        model = Sequential()

        model.add(Flatten(input_shape=self.img_shape))
        model.add(Dense(self.node_scale_factor * 2))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(self.node_scale_factor))
        model.add(LeakyReLU(alpha=0.2))
        model.add(Dense(1, activation="sigmoid"))
        model.summary()

        img = Input(shape=self.img_shape)
        validity = model(img)

        return Model(img, validity)

    def train(self, epochs, batch_size=128, sample_interval=50):

        # Load the dataset
        X_train = self.input_data

        # Rescale -1 to 1
        # X_train = X_train / 127.5 - 1.  #TODO
        X_train = np.expand_dims(X_train, axis=3)

        # Adversarial ground truths
        valid = np.ones((batch_size, 1))
        fake = np.zeros((batch_size, 1))

        for epoch in range(epochs):

            # ---------------------
            #  Train Discriminator
            # ---------------------

            # Select a random batch of images
            idx = np.random.randint(0, X_train.shape[0], batch_size)
            imgs = X_train[idx]

            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

            # Generate a batch of new images
            gen_imgs = self.generator.predict(noise)

            # Train the discriminator
            d_loss_real = self.discriminator.train_on_batch(imgs, valid)
            d_loss_fake = self.discriminator.train_on_batch(gen_imgs, fake)
            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            # ---------------------
            #  Train Generator
            # ---------------------

            noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

            # Train the generator (to have the discriminator label samples as valid)
            g_loss = self.combined.train_on_batch(noise, valid)

            # Plot the progress
            print(
                "%d [D loss: %f, acc.: %.2f%%] [G loss: %f]"
                % (epoch, d_loss[0], 100 * d_loss[1], g_loss)
            )

            # If at save interval => save generated image samples
            if epoch % sample_interval == 0:
                self.save_sample_images(epoch)

        self.save_sample_images(epoch)
        self.save_model()

    def save_model(self):
        self.discriminator.save(self.discriminator_path)
        self.generator.compile(loss="binary_crossentropy", optimizer=Adam(0.0002, 0.5))
        self.generator.save(self.generator_path)

    def load_models(self):
        self.generator = load_model(self.generator_path)

    def sample_image(self):
        noise = np.random.normal(0, 1, (1, self.latent_dim))
        print(noise.shape)
        image = self.generator.predict(noise)
        image = np.reshape(image, self.img_shape[0:2])
        image = 0.5 * image + 0.5
        image = image > 0.9
        return image

    def save_sample_images(self, epoch):
        r, c = 5, 5
        noise = np.random.normal(0, 1, (r * c, self.latent_dim))
        gen_imgs = self.generator.predict(noise)

        # Rescale images 0 - 1
        gen_imgs = self.rescale_image_values(gen_imgs)
        gen_imgs = 0.5 * gen_imgs + 0.5

        fig, axs = plt.subplots(r, c)
        cnt = 0
        for i in range(r):
            for j in range(c):
                axs[i, j].imshow(gen_imgs[cnt, :, :, 0], cmap="gray")
                axs[i, j].axis("off")
                cnt += 1
        fig.savefig("images/%d.png" % epoch)
        plt.close()


if __name__ == "__main__":
    gan = GAN()
    gan.train(epochs=1000, batch_size=32, sample_interval=50)
