from __future__ import print_function

import tensorflow as tf

import argparse
import os
from six.moves import cPickle

from model import Model

from six import text_type

def get_default_args():

    parser = argparse.ArgumentParser(
                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--save_dir', type=str, default='save',
                        help='model directory to store checkpointed models')
    parser.add_argument('-n', type=int, default=500,
                        help='number of characters to sample')
    parser.add_argument('--prime', type=text_type, default=u'A',
                        help='prime text')
    parser.add_argument('--sample', type=int, default=1,
                        help='0 to use max at each timestep, 1 to sample at '
                             'each timestep, 2 to sample on spaces')
    return parser


def main():
    parser = get_default_args()
    args = parser.parse_args()
    print(sample(args))


def get_sample(base_save_dir,sample_length,seed_str):
    # This function exposes the arguments that would normally be run from the command line.
    # It is used so that other parts of the python program can access stuff
    parser = get_default_args()
    args = parser.parse_args()
    args.save_dir = base_save_dir
    args.n = sample_length
    args.prime = seed_str
    return sample(args)


def sample(args):
    with open(os.path.join(args.save_dir+'save/', 'config.pkl'), 'rb') as f:
        saved_args = cPickle.load(f)
    with open(os.path.join(args.save_dir+'save/', 'chars_vocab.pkl'), 'rb') as f:
        chars, vocab = cPickle.load(f)
    model = Model(saved_args, training=False)
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        saver = tf.train.Saver(tf.global_variables())
        ckpt = tf.train.get_checkpoint_state(args.save_dir+'save/')
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            return model.sample(sess, chars, vocab, args.n, args.prime, args.sample)

if __name__ == '__main__':
    main()
