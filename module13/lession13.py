from itertools import product

import numpy as np

import pandas as pd


# arr_2d = np.array ([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr_2d)
#
# element = arr_2d[1,2]
# print(element)

product = ["apple", "peach", "cherry", "orange"]
sales = [12, 40, 100, 120 ]

product_seris = pd.series(sales, index=(product))

total_series
