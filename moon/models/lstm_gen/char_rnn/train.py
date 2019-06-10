import codecs
import collections
import os
import pickle
import time

import numpy as np
import tensorflow as tf
from six.moves import cPickle

from moon.models.lstm_gen.char_rnn.model import Model


class TextLoader:
    def __init__(self, data_dir, batch_size, seq_length, encoding="utf-8"):
        self.data_dir = data_dir
        self.batch_size = batch_size
        self.seq_length = seq_length
        self.encoding = encoding

        input_file = os.path.join(data_dir, "input.txt")
        vocab_file = os.path.join(data_dir, "vocab.pkl")
        tensor_file = os.path.join(data_dir, "data.npy")

        if not (os.path.exists(vocab_file) and os.path.exists(tensor_file)):
            print("reading text file")
            self.preprocess(input_file, vocab_file, tensor_file)
        else:
            print("loading preprocessed files")
            self.load_preprocessed(vocab_file, tensor_file)
        self.create_batches()
        self.reset_batch_pointer()

    def preprocess(self, input_file, vocab_file, tensor_file):
        with codecs.open(input_file, "r", encoding=self.encoding) as f:
            data = f.read()
        counter = collections.Counter(data)
        count_pairs = sorted(counter.items(), key=lambda x: -x[1])
        self.chars, _ = zip(*count_pairs)
        self.vocab_size = len(self.chars)
        self.vocab = dict(zip(self.chars, range(len(self.chars))))
        with open(vocab_file, "wb") as f:
            cPickle.dump(self.chars, f)
        self.tensor = np.array(list(map(self.vocab.get, data)))
        np.save(tensor_file, self.tensor)

    def load_preprocessed(self, vocab_file, tensor_file):
        with open(vocab_file, "rb") as f:
            self.chars = cPickle.load(f)
        self.vocab_size = len(self.chars)
        self.vocab = dict(zip(self.chars, range(len(self.chars))))
        self.tensor = np.load(tensor_file)
        self.num_batches = int(self.tensor.size / (self.batch_size * self.seq_length))

    def create_batches(self):
        self.num_batches = int(self.tensor.size / (self.batch_size * self.seq_length))

        # When the data (tensor) is too small,
        # let's give them a better error message
        if self.num_batches == 0:
            assert False, "Not enough data. Make seq_length and batch_size small."

        self.tensor = self.tensor[: self.num_batches * self.batch_size * self.seq_length]
        xdata = self.tensor
        ydata = np.copy(self.tensor)
        ydata[:-1] = xdata[1:]
        ydata[-1] = xdata[0]
        self.x_batches = np.split(xdata.reshape(self.batch_size, -1), self.num_batches, 1)
        self.y_batches = np.split(ydata.reshape(self.batch_size, -1), self.num_batches, 1)

    def next_batch(self):
        x, y = self.x_batches[self.pointer], self.y_batches[self.pointer]
        self.pointer += 1
        return x, y

    def reset_batch_pointer(self):
        self.pointer = 0


def build_model(base_save_dir):
    with open("train_args.pickle", "rb") as my_data_file:
        args = pickle.load(my_data_file)
    # alter it according to the custom parameters
    args.save_every = 20000
    args.num_epochs = 5
    args.data_dir = base_save_dir
    train(args)


def train(args):
    data_loader = TextLoader(args.data_dir, args.batch_size, args.seq_length)
    args.vocab_size = data_loader.vocab_size

    # check compatibility if training is continued from previously saved model
    if args.init_from is not None:
        # check if all necessary files exist
        assert os.path.isdir(args.init_from), " %s must be a a path" % args.init_from
        assert os.path.isfile(os.path.join(args.init_from, "config.pkl")), (
            "config.pkl file does not exist in path %s" % args.init_from
        )
        assert os.path.isfile(os.path.join(args.init_from, "chars_vocab.pkl")), (
            "chars_vocab.pkl.pkl file does not exist in path %s" % args.init_from
        )
        ckpt = tf.train.get_checkpoint_state(args.init_from)
        assert ckpt, "No checkpoint found"
        assert ckpt.model_checkpoint_path, "No model path found in checkpoint"

        # open old config and check if models are compatible
        with open(os.path.join(args.init_from, "config.pkl"), "rb") as f:
            saved_model_args = cPickle.load(f)
        need_be_same = ["model", "rnn_size", "num_layers", "seq_length"]
        for checkme in need_be_same:
            assert vars(saved_model_args)[checkme] == vars(args)[checkme], (
                "Command line argument and saved model disagree on '%s' " % checkme
            )

        # open saved vocab/dict and check if vocabs/dicts are compatible
        with open(os.path.join(args.init_from, "chars_vocab.pkl"), "rb") as f:
            saved_chars, saved_vocab = cPickle.load(f)
        assert saved_chars == data_loader.chars, "Data and loaded model disagree on character set!"
        assert (
            saved_vocab == data_loader.vocab
        ), "Data and loaded model disagree on dictionary mappings!"

    save_dir = os.path.join(args.data_dir, "save")
    if not os.path.isdir(save_dir):
        os.makedirs(save_dir)
    with open(os.path.join(save_dir, "config.pkl"), "wb") as f:
        cPickle.dump(args, f)
    with open(os.path.join(save_dir, "chars_vocab.pkl"), "wb") as f:
        cPickle.dump((data_loader.chars, data_loader.vocab), f)

    model = Model(args)

    with tf.Session() as sess:
        # instrument for tensorboard
        summaries = tf.summary.merge_all()
        writer = tf.summary.FileWriter(
            os.path.join(os.path.join(args.data_dir, "logs"), time.strftime("%Y-%m-%d-%H-%M-%S"))
        )
        writer.add_graph(sess.graph)

        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver(tf.global_variables())
        # restore model
        if args.init_from is not None:
            saver.restore(sess, ckpt.model_checkpoint_path)
        for e in range(args.num_epochs):
            sess.run(tf.assign(model.lr, args.learning_rate * (args.decay_rate ** e)))
            data_loader.reset_batch_pointer()
            state = sess.run(model.initial_state)
            for b in range(data_loader.num_batches):
                start = time.time()
                x, y = data_loader.next_batch()
                feed = {model.input_data: x, model.targets: y}
                for i, (c, h) in enumerate(model.initial_state):
                    feed[c] = state[i].c
                    feed[h] = state[i].h

                # instrument for tensorboard
                summ, train_loss, state, _ = sess.run(
                    [summaries, model.cost, model.final_state, model.train_op], feed
                )
                writer.add_summary(summ, e * data_loader.num_batches + b)

                end = time.time()
                print(
                    "{}/{} (epoch {}), train_loss = {:.3f}, time/batch = {:.3f}".format(
                        e * data_loader.num_batches + b,
                        args.num_epochs * data_loader.num_batches,
                        e,
                        train_loss,
                        end - start,
                    )
                )
                if (e * data_loader.num_batches + b) % args.save_every == 0 or (
                    e == args.num_epochs - 1 and b == data_loader.num_batches - 1
                ):
                    # save for the last result
                    checkpoint_path = os.path.join(args.data_dir, "save/", "model.ckpt")
                    saver.save(sess, checkpoint_path, global_step=e * data_loader.num_batches + b)
                    print("model saved to {}".format(checkpoint_path))
