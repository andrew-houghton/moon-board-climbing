from __future__ import print_function

import random

import numpy as np
from keras.callbacks import LambdaCallback
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.optimizers import RMSprop

from moon.types.climb import Climb
from moon.types.climbset import Climbset


class Model:
    def prep_data(self, training_climbset):
        text = training_climbset.no_grade_string()
        chars = sorted(list(set(text)))
        print("total chars:", len(chars))
        char_indices = dict((c, i) for i, c in enumerate(chars))
        indices_char = dict((i, c) for i, c in enumerate(chars))
        return text, chars, char_indices, indices_char

    def clean_sample(self, sample):
        split_sample = sample.split(Climbset.get_terminator())

        # Clean up items at the end
        if len(split_sample[0]) <= 1:
            # remove first item if it is too short to be a climb
            split_sample.pop(0)
        split_sample.pop(len(split_sample) - 1)

        return [
            climb_str
            for climb_str in split_sample
            if Climb.valid_input_sample(climb_str)
        ]

    def train(self, training_climbset, params):
        maxlen = params.max_climb_length
        text, chars, char_indices, indices_char = self.prep_data(
            training_climbset
        )
        # cut the text in semi-redundant sequences of maxlen characters
        step = 3
        sentences = []
        next_chars = []
        for i in range(0, len(text) - maxlen, step):
            sentences.append(text[i : i + maxlen])
            next_chars.append(text[i + maxlen])
        print("nb sequences:", len(sentences))

        print("Vectorization...")
        x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
        y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
        for i, sentence in enumerate(sentences):
            for t, char in enumerate(sentence):
                x[i, t, char_indices[char]] = 1
            y[i, char_indices[next_chars[i]]] = 1

        # build the model: a single LSTM
        print("Build model...")
        self.model = Sequential()
        assert len(params.num_lstm_cells) == 1
        self.model.add(
            LSTM(params.num_lstm_cells[0], input_shape=(maxlen, len(chars)))
        )
        self.model.add(Dense(len(chars), activation="softmax"))

        self.model.compile(
            loss="categorical_crossentropy", optimizer=params.optimizer
        )
        return self.model.fit(
            x, y, batch_size=params.batch_size, epochs=params.epochs
        )

    def sample(self, training_climbset, num_climbs, params):
        self.train(training_climbset, params)
        return self._take_sample(training_climbset, num_climbs, params)

    def _take_sample(self, training_climbset, num_climbs, params):
        def _sample_from_array(preds, temperature=0.8):
            # helper function to sample an index from a probability array
            preds = np.asarray(preds).astype("float64")
            preds = np.log(preds) / temperature
            exp_preds = np.exp(preds)
            preds = exp_preds / np.sum(exp_preds)
            probas = np.random.multinomial(1, preds, 1)
            return np.argmax(probas)

        def _generate_text():
            text, chars, char_indices, indices_char = self.prep_data(
                training_climbset
            )

            start_index = random.randint(
                0, len(text) - params.max_climb_length - 1
            )
            generated = ""
            sentence = text[
                start_index : start_index + params.max_climb_length
            ]
            generated += sentence

            for i in range(num_climbs * 25):
                x_pred = np.zeros((1, params.max_climb_length, len(chars)))
                for t, char in enumerate(sentence):
                    x_pred[0, t, char_indices[char]] = 1.0

                preds = self.model.predict(x_pred, verbose=0)[0]
                next_index = _sample_from_array(preds, temperature=0.8)
                next_char = indices_char[next_index]

                generated += next_char
                sentence = sentence[1:] + next_char

            return generated

        generated_sample = self.clean_sample(_generate_text())
        generated_climbs = Climbset(generated_sample, "sample")

        print(
            f"Generated {len(generated_climbs.climbs)} and kept {num_climbs}."
        )
        generated_climbs.climbs = generated_climbs.climbs[:num_climbs]

        return generated_climbs
