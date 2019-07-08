from dataclasses import dataclass
from typing import Optional

import numpy as np
from sklearn.metrics import accuracy_score


def expected_diff(test_data, score_data):
    ex_sum_diff = sum([abs(test_data[i] - score_data[i]) for i in range(len(test_data))])
    return ex_sum_diff / len(test_data)


def within_k(actual, sample, k):
    assert type(actual) == np.ndarray
    item_type = type(actual[0])

    if item_type == np.int64:
        num = ((actual - sample) <= k).sum()
        return num / len(actual)
    elif item_type == np.ndarray:
        actual = actual.argmax(axis=1)
        sample = sample.argmax(axis=1)

        num = ((actual - sample) <= k).sum()
        return num / len(actual)
    else:
        return 0.0


@dataclass
class Metrics:
    accuracy: Optional[float] = None
    within_1: Optional[float] = None
    within_2: Optional[float] = None

    def generate_metrics(self, actual, sample):
        self.accuracy = accuracy_score(actual, sample)
        self.within_1 = within_k(actual, sample, 1)
        self.within_2 = within_k(actual, sample, 2)
