import numpy as np

temperatures = np.array([
    29.3, 42.1, 18.8, 38.0, 12.5,
    12.6, 49.6, 38.8, 31.3, 9.2, 22.2
]).reshape(2,2,3)

temperatures.shape

temperatures

np.swapaxes(temperatures, 1, 2)