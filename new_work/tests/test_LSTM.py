import unittest
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/util'
sys.path.append(import_path)
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/types'
sys.path.append(import_path)

import sample_LSTM
from climb import Climb

class TestSampling(unittest.TestCase):

    def testPregradeSample(self):
        new_sample = sample_LSTM.sample_model('pre_grade')
        self.assertTrue(type(new_sample) == str)

        cleaned_sample = sample_LSTM.clean_sample(new_sample)
        print(cleaned_sample)
        print(cleaned_sample[0])
        first_sample_climb = Climb('sample',cleaned_sample[0])
        print(first_sample_climb)

if __name__ == '__main__':
    unittest.main(verbosity=1)
