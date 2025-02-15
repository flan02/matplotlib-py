import numpy as np
import matplotlib.pyplot as plt
import os

ax = plt.axes(projection='3d')

x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z, cmap='viridis') # cmap='viridis' is the default color map, cmap='coolwarm' is another option or cmap='plasma', cmap='Spectral'
ax.set_title('Surface Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

ax.view_init(azim=0, elev=90) 

filename = 'graphs/surface_plot.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}')
else:
    print('Filename already exists. Image not saved.')

plt.show()