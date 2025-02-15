import numpy as np
import matplotlib.pyplot as plt
import os

stock_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stock_b = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
stock_c = [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

plt.plot(stock_a, label='Stock A')
plt.plot(stock_b, label='Stock B')
plt.plot(stock_c, label='Stock C')

plt.legend(loc="upper left")
plt.show()