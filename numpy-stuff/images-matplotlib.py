import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("https://files.realpython.com/media/kitty.90952ca484f1.jpg")
print(type(img))
>>> <class 'numpy.ndarray'>

print(img.shape)
>>> (1299, 1920, 3)

""" Create blue img
output = img.copy()
output[:, :, :2] = 0
mpimg.imsave("blue.jpg", output)
"""

"""first attempt at gre/ayscale
averages = img.mean(axis=2)
mpimg.imsave("bad-grey.jpg", averages, cmap="gray")"""

weights = np.array([0.3, 0.59, 0.11])
grayscale = img @ weights
mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")