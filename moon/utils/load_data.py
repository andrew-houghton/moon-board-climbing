import os
import pickle


def numpy():
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    numpypath = os.path.join(scriptpath, "numpy.pkl")
    return pickle.load(open(numpypath, "rb"))
