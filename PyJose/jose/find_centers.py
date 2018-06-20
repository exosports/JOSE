import numpy as np
from scipy.optimize import curve_fit, least_squares

import matplotlib.pyplot as plt

def find_centers(data):
    '''Returns a value for the center for each row of input data'''
    centers = np.zeros(data.shape[0])

    gaussian = lambda x, a, b, c, d: a * np.exp(-(x - b)**2 / c**2) + d


    x = list(range(len(data[0])))
    for i, row in enumerate(data):
        # make own function? unit test?
        popt, pcov = curve_fit(gaussian, x, row, p0=(np.max(row), len(x)/2, 1, np.min(row)))
        centers[i] = popt[1]
        plt.plot(x, row)
        plt.plot(x, gaussian(x, *popt))
        plt.show()

    return centers
