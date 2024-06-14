import numpy as np

prices = [50.5, 49.5, 25.1, 74.9]

"""
mean - returns the average value of the array.
std - returns the standard deviation
sum - returns the sum of all values
max - returns the maximum value.
"""
print(np.mean(prices))  # result = 50

print(np.std(prices))  # result = 17.61050822662424

print(np.sum(prices))  # result = 200

print(np.max(prices))  # result = 75.9
