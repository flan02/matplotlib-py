import numpy as np
import matplotlib.pyplot as plt
import os

x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

# - window 1
plt.figure(1)
plt.scatter(x1,y1)

# - window 2
plt.figure(2)
plt.bar(x2,y2)

filename = 'graphs/multiple_figures.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}')
else:
    print('Filename already exists. Image not saved.')

plt.show()