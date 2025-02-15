import numpy as np
import matplotlib.pyplot as plt
import os

#heights = np.random.normal(172, 8, 300)
#plt.boxplot(heights)

first = np.linspace(0,10,25)
second = np.linspace(10,200,25)
third = np.linspace(200,210,25)
fourth = np.linspace(210,230,25)

data = np.concatenate((first, second, third, fourth))

plt.boxplot(data)

filename = 'graphs/box_plots2.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}')
else:
    print('Filename already exists. Image not saved.')


plt.show()