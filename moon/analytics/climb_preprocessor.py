import numpy as np
from keras.preprocessing import sequence


class OneHotPreprocessor:
    def preprocess(self, climbs):
        climbs = np.asarray([np.asarray(climb.as_image()) for climb in climbs])
        return np.reshape(climbs, (len(climbs), 11 * 18)).astype(int)


class HoldListPreprocessor:
    def _hold_list(self, climb):
        return [(hold.col, hold.row) for hold in climb.holds]

    def _move_sizes(self, hold_list):
        hold_queue = [hold_list[0]]

        for i in range(len(hold_list) - 1):
            hold = hold_list[i]
            next_hold = hold_list[i + 1]
            hold_queue.append(tuple(i - j for i, j in zip(next_hold, hold)))
            hold_queue.append(next_hold)
        return hold_queue

    def preprocess(self, climbs):
        holds = list(map(self._hold_list, climbs))
        # holds_and_moves = list(map(move_sizes, holds))
        return sequence.pad_sequences(holds, maxlen=12)
