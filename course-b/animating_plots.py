import numpy as np
import matplotlib.pyplot as plt
import os

import random

heads_tails = [0,0]

for _ in range(100000):
    heads_tails[random.randint(0,1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=['blue', 'red'])
    plt.title('Coin Toss')
    plt.xlabel('Coin Side')
    plt.ylabel('Number of Tosses')
    plt.pause(0.001)
    #plt.clf() # clear figure

plt.show()