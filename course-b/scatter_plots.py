import numpy as np
import matplotlib.pyplot as plt
import os

x = np.random.random(50) * 100
y = np.random.random(50) * 100

plt.scatter(x, y, c='red', marker='*')

filename = 'scatter_plot.png'

if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')

plt.show()