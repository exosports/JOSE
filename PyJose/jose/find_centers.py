import numpy as np
from scipy.optimize import curve_fit, least_squares
from astropy.stats import sigma_clip
from astropy.modeling import models, fitting
import scipy.stats as stats

import matplotlib.pyplot as plt

def jose_fit(x, row, variance):


def scipy_fit(x, row, variance):
    gaussian = lambda x, a, b, c, d: a * np.exp(-(x - b) ** 2 / c ** 2) + d
    f = lambda params, x, y: gaussian(x, *params) - y
    initial_parameters = (np.max(row), len(x) / 2, 1, np.min(row)) # create reasonable initial guesses
        # make own function?  unit test?
    optimization = least_squares(f, initial_parameters, loss='soft_l1', f_scale=0.1, args=(x, row))
    results = gaussian(x, *optimization.x)
    return optimization.x[1]

def astropy_clipping_fit(x, row, variance):
    gauss_model = models.Gaussian1D() + models.Const1D()

    fit = fitting.LevMarLSQFitter()
    clipping_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip, niter=30, sigma=15.0)

    # initialize fitters
    fit = fitting.LevMarLSQFitter()
    or_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip,
                                           niter=3, sigma=6.0)

    g_init = models.Gaussian1D(amplitude=np.max(row),
                                  mean=len(x) / 2, 
                                  stddev=1.0) + models.Const1D(amplitude=np.min(row))
    filtered_data, or_fitted_model = or_fit(g_init, x, row, weights=1.0 / variance)
    return or_fitted_model.mean_0.value

def basic_curve_fit(x, row, variance):
    gaussian = lambda x, a, b, c, d: a * np.exp(-(x - b) ** 2 / c ** 2) + d
    popt, pcov = curve_fit(gaussian, x, row, p0=(np.max(row), len(x) / 2, 1, np.min(row)))
    return popt[1] 

def find_centers(data, variance, left_bound, right_bound):
    '''Returns a value for the center for each row of input data'''
    centers = np.zeros(data.shape[0])

    x = np.array(list(range(len(data[0, left_bound:right_bound]))))
    for i, row in enumerate(data[:, left_bound:right_bound]):
        
        centers[i] = left_bound + astropy_clipping_fit(x, row, variance[i, left_bound:right_bound])

        #plt.plot(x, row, 'gx')
        #plt.plot(x, filtered_data, 'r+')
        #plt.plot(x, or_fitted_model(x))
        #plt.show()

    return centers
