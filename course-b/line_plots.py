import numpy as np
import matplotlib.pyplot as plt
import os

years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 82, 81, 79, 83, 80,
           82, 82, 83, 81, 80, 79 ]

plt.plot(years, weights, marker='o', linestyle='--', c='green')

filename = 'graphs/line_plot.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')


plt.show()