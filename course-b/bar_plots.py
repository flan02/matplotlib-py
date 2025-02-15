import numpy as np
import matplotlib.pyplot as plt
import os

x=["C++","C#","Python","Java","Go"]
y=[20,50,140,10,45]

plt.bar(x,y, align='edge', width=0.2, edgecolor='black', lw=3)

filename = 'graphs/bar_plot.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')


plt.show()