import numpy as np
import matplotlib.pyplot as plt
import os

ages = np.random.normal(20, 1.5, 1000)

plt.hist(ages,
         bins=[ages.min(), 18, 21, ages.max()] # bins are the edges of the bars
         )


filename = 'graphs/histogram.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')


plt.show()