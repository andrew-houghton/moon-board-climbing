from classes import Hold
from classes import Climb
import utilities

max_climb_length = Climb.get_max_len()
hold_dimension = Hold.get_data_len()
cell = 100  # TODO what should this be?
batch_size = 1024


def load_climbs_from_file(file_path):
    ''' Loads the climbs from a given path.
    Works with the padded_climbs.txt file
    Returns a list of objects of the Climb class'''

    # Open the file
    with open(file_path, 'r') as f:
        raw_climbs = f.read()
    raw_climbs = raw_climbs.split(utilities.climb_seperator)  # split climbs up

    # Look at every climb, process it into the a climb object
    climbs = []
    for climb in raw_climbs:
        hold_array = []
        for hold_num in range(Climb.get_max_len()):
            move_txt = climb[hold_num * 2:hold_num * 2 + 2]
            if move_txt != '__':
                move_numbers = (ord(move_txt[0]) - utilities.col_char_base - 1,
                                ord(move_txt[1]) - utilities.num_base - 2)
                # numbers between 0 and 1
                XY = utilities.normalize_XY(move_numbers)

                hold_array.append(Hold(XY))
            else:
                # padding hold.
                hold_array.append(Hold())
        climbs.append([list(i.get_data()) for i in hold_array])
    return climbs


def custom_metric(y_true, y_pred):
    return abs(y_pred - y_true)

def custom_metric_2(y_true,y_pred):
    #if y_pred rounds into y_true then output 1 else output 0
    return 0

def make_model():
    from keras.models import Sequential
    from keras.layers import Dense
    # from keras.layers import Dropout
    from keras.layers import LSTM

    model = Sequential()
    # Input goes into the LSTM as holds in a series
    model.add(LSTM(cell, batch_input_shape=(
        batch_size, max_climb_length, hold_dimension)))
    # Output has 3 values # TODO should there be an activation function?
    model.add(Dense(hold_dimension))
    model.compile(loss='mean_squared_error',
                  optimizer='adam', metrics=['accuracy', custom_metric])
    return model

climbs = load_climbs_from_file('../climb_text/padded_climbs.txt')

import numpy as np
print(np.array(climbs).shape)

joined = []
for i in climbs:
    joined += i

print(np.array(joined).shape)

x_train = []
y_train = []

num_climbs = len(joined) - max_climb_length
num_climbs = num_climbs - num_climbs % batch_size

for i in range(num_climbs):
    x_train.append(joined[
        i:i + max_climb_length])
    y_train.append(joined[
        i + max_climb_length])

print(np.array(x_train).shape)
print(np.array(y_train).shape)

epochs = 6
print('Creating model.')
model = make_model()
print('Starting training.')
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)

model.save_weights('my_model.hdf5')