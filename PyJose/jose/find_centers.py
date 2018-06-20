import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

def find_centers(data):
    '''Returns a value for the center for each row of input data'''
    centers = np.zeros(data.shape[0])

    gaussian = lambda x, a, b, c: a * np.exp(-(x - b)**2 / c**2)

    x = list(range(len(data[0])))
    for i, row in enumerate(data):
        popt, pcov = curve_fit(gaussian, x, row, loss='soft_l1')
        centers[i] = popt[1]
        plt.plot(x, row)
        plt.plot(x, gaussian(x, *popt))
        plt.show()

    return centers
