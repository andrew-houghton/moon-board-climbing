from keras.datasets import mnist
import pickle
import numpy as np
from matplotlib import pyplot as plt

climbs = pickle.load(open('numpy.pkl', 'rb'))
climbs = np.array(climbs)
climbs = climbs[:, :, :11]

plt.imshow(climbs[0], interpolation='nearest')
plt.show()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(x_train.shape)
print(x_test.shape)
print(climbs.shape)
