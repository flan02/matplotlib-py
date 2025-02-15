import numpy as np
import matplotlib.pyplot as plt
import os

ax = plt.axes(projection='3d')

# x = np.random.random(100)
# y = np.random.random(100)
# z = np.random.random(100)
# ax.scatter(x,y,z)

# - 2D PLOT
x = np.arange(0,50,0.1)
y = np.arange(0,50,0.1)
z = np.cos(x+y)

# - 3D PLOT
# x = np.arange(0,50,0.1)
# y = np.sin(x)
# z = np.cos(x)

ax.plot(x,y,z)
ax.set_title('3d Plot')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

filename = 'graphs/three-dim_plot.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')

plt.show()