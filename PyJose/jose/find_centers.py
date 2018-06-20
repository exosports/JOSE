import numpy as np
from scipy.optimize import curve_fit, least_squares
from astropy.stats import sigma_clip
from astropy.modeling import models, fitting
import scipy.stats as stats

import matplotlib.pyplot as plt

def find_centers(data, variance):
    '''Returns a value for the center for each row of input data'''
    centers = np.zeros(data.shape[0])

    #gaussian = lambda x, a, b, c, d: a * np.exp(-(x - b)**2 / c**2) + d
    gauss_model = models.Gaussian1D() + models.Const1D()

    #f = lambda params, x, y: gaussian(x, *params) - y

    fit = fitting.LevMarLSQFitter()
    clipping_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip, niter=30, sigma=3.0)


    # initialize fitters
    fit = fitting.LevMarLSQFitter()
    or_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip,
                                           niter=3, sigma=6.0)

    left_bound = 200
    right_bound = 300

    x = np.array(list(range(len(data[0]))))
    for i, row in enumerate(data):
        g_init = models.Gaussian1D(amplitude=np.max(row[left_bound:right_bound]), mean=len(x)/2, stddev=1.) + models.Const1D(amplitude=np.min(row))
        # initial_parameters = (np.max(row), len(x) / 2, 1, np.min(row)) # create reasonable initial guesses
        # make own function? unit test?
        #masked_data, model = clipping_fit(gauss_model, x, row)
        filtered_data, or_fitted_model = or_fit(g_init, x, row, weights=1.0/variance[i, :])

        centers[i] = or_fitted_model.mean_0.value

        #plt.plot(x, row, 'gx')
        #plt.plot(x, filtered_data, 'r+')
        #plt.plot(x, or_fitted_model(x))
        #plt.show()




        #popt, pcov = curve_fit(gaussian, x, row, p0=(np.max(row), len(x)/2, 1, np.min(row)))
        #centers[i] = popt[1]
        #plt.plot(x, row)
        #plt.plot(x, gaussian(x, *popt))
        #plt.show()

    return centers
