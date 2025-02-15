import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import os

style.use('dark_background')

langs = ['Python', 'C++', 'Ruby', 'Java', 'Typescript']

votes = [50, 24, 14, 6, 17]
explodes = [0,0,0,0.2,0]

plt.pie(votes, labels=None, explode= explodes, autopct='%.2f%%', pctdistance=0.8, startangle=90)
plt.legend(labels=langs)

filename = 'graphs/pie_charts2.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')


plt.show()