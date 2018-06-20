import numpy as np
from scipy.optimize import curve_fit, least_squares
from astropy.stats import sigma_clip
from astropy.modeling import models, fitting
import scipy.stats as stats

import matplotlib.pyplot as plt

def find_centers(data, variance):
    '''Returns a value for the center for each row of input data'''
    centers = np.zeros(data.shape[0])

    gaussian = lambda x, a, b, c, d: a * np.exp(-(x - b)**2 / c**2) + d

    f = lambda params, x, y: gaussian(x, *params) - y


    x = list(range(len(data[0])))
    for i, row in enumerate(data):
        initial_parameters = (np.max(row), len(x) / 2, 1, np.min(row)) # create reasonable initial guesses
        # make own function? unit test?
        optimization = least_squares(f, initial_parameters, loss='soft_l1', f_scale=0.1, args=(x, row))
        results = gaussian(x, *optimization.x)

        plt.plot(x, row, x, results)
        plt.show()




        #popt, pcov = curve_fit(gaussian, x, row, p0=(np.max(row), len(x)/2, 1, np.min(row)))
        #centers[i] = popt[1]
        #plt.plot(x, row)
        #plt.plot(x, gaussian(x, *popt))
        #plt.show()

    return centers
