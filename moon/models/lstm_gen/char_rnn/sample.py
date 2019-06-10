import os
import pickle

import tensorflow as tf
from six.moves import cPickle

from moon.models.lstm_gen.char_rnn.model import Model


def get_sample(base_save_dir, sample_length, seed_str):
    with open("sample_args.pickle", "rb") as handle:
        args = pickle.load(handle)
    args.save_dir = base_save_dir
    args.n = sample_length
    args.prime = seed_str
    return sample(args)


def sample(args):
    with open(os.path.join(args.save_dir, "save/", "config.pkl"), "rb") as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir, "save/", "chars_vocab.pkl"), "rb") as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, training=False)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(os.path.join(args.save_dir, "save/"))
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            return model.sample(sess, chars, vocab, args.n, args.prime, args.sample)
