import numpy as np
import matplotlib.pyplot as plt
import os

years = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

income = [55,56,62,61,72,72,73,75]

income_ticks = list(range(50, 81, 2))

plt.plot(years, income)
plt.title('Income of John (USD)', fontsize=30)

plt.xlabel('Year')
plt.ylabel('Yearly Income in (USD)')
plt.yticks(income_ticks, [f"${x}k" for x in income_ticks])

filename = 'graphs/plot_customization.png'
if not os.path.exists(filename):
    plt.savefig(filename, dpi=300)
    print(f'Image saved as {filename}.')
else:
    print('Filename already exists. Image not saved.')

plt.show()