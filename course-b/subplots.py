import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(100)

fig, axs = plt.subplots(2, 2) # 2x2 grid

# Plotting on each subplot
# We obtain 4 graphs in a 2x2 grid

axs[0,0].plot(x, np.sin(x))
axs[0,0].set_title('Sine wave')

axs[0,1].plot(x, np.cos(x))
axs[0,1].set_title('Cosine wave')

axs[1,0].plot(x, np.random.random(100))
axs[1,0].set_title('Random function')

axs[1,1].plot(x, np.log(x))
axs[1,1].set_title('log function')
axs[1,1].set_xlabel('Test')

fig.suptitle('Four Plots')

filename = 'graphs/subplots.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300) # transparent=False, bbox_inches='tight'
    print(f'Image saved as {filename}')
else:
    print('Filename already exists. Image not saved.')

plt.show()
