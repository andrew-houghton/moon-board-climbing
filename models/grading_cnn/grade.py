import pickle
import models.grading_cnn.model as model
import os


base_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
pickle_filepath = base_directory+"/data/numpy/numpy.pkl"

with open(pickle_filepath, 'rb') as handle:
    climbs=pickle.load(handle)

print(len(climbs))
