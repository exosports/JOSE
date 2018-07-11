import numpy as np
import logging
from astropy.modeling import models, fitting
from astropy.stats import sigma_clip

log = logging.getLogger(__name__)

def single_sigma_clip(data, *args):
    pass

def procvect(xdata, ydata, variance, threshold, fit_type, absolute_threshold, kwargs):
    '''docstring'''
    polynomial = models.Polynomial1D(degree=1)
    fit = fitting.LevMarLSQFitter()
    outliersRemoved_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip)

    a, b = fit(polynomial, xdata, ydata, weights=1.0 / variance)
    filtered_data, model = outliersRemoved_fit(polynomial, xdata, ydata, weights = 1.0 / variance)

    return model(xdata), None, model



#def procvect(xdata, ydata, variance, threshold, fit_type, absolute_threshold, kwargs):
#    '''docstring'''
#    outliers_remaining = True
#    mask = np.full(np.shape(xdata), True)
#    previous_outliers = None

#    while outliers_remaining:
#        # TODO: refactor for better fit_type
#        if fit_type == 'polynomial':
#            # TODO: I think the weights are messed up, maybe should be sqrt of that
#            coeff = np.polyfit(xdata[mask], ydata[mask], **kwargs, w = 1 / variance[mask])
#            model = np.poly1d(coeff)
#            fitted_values = model(xdata)
#            # check for outliers

#            # TODO: absolute threshold
#            outliers = (fitted_values - ydata)**2 / (variance) > threshold

#            if not np.array_equal(outliers, previous_outliers):
#                # check if set of outliers has changed between iterations, quit when it stabalizes
#                previous_outliers = outliers
#                mask[outliers] = False
#            else:
#                outliers_remaining = False
#    return model(xdata), mask, model
