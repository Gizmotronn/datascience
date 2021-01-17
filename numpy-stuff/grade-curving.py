import numpy as np
CURVE_CENTER = 80
grades = np.array([72, 35, 64, 88, 51, 90, 74, 12]) # one-dimensional array. Shape of (8,). Data type int64. 
def curve(grades): # taking grades array as a param
	average = grades.mean() # mean method of grades
	change = CURVE_CENTER - average
	new_grades = grades + change # vectorization - performs the same operation for every element in the array. Also includes Broadcasting
	return np.clip(new_grades, grades, 100) # limit/clip the values to a set of minimum and maximums. Can't go lower than the original grade or higher than 100

curve(grades)
