from dataclasses import dataclass
from typing import Optional
from sklearn.metrics import accuracy_score


def expected_diff(test_data, score_data):
    ex_sum_diff = sum([abs(test_data[i] - score_data[i]) for i in range(len(test_data))])
    return ex_sum_diff / len(test_data)


@dataclass
class Metrics:
    accuracy: Optional[float] = None

    def generate_metrics(self, actual, sample):
        self.accuracy = accuracy_score(actual, sample)
