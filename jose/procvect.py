import numpy as np
import logging
from astropy.modeling import models, fitting
from astropy.stats import sigma_clip

log = logging.getLogger(__name__)

def single_sigma_clip(data, *args):
    pass

def procvect(xdata, ydata, variance, threshold, fit_type,
             absolute_threshold, kwargs):
    '''Reject only one pixel at a time'''
    converged = False
    mask = np.full(np.shape(xdata), True)

    while not converged:
        if fit_type == 'polynomial':
            x_masked = xdata[mask]
            y_masked = ydata[mask]
            variance_masked = variance[mask]
            # TODO: I think the weights are messed up,
            # maybe should be sqrt of that
            coeff = np.polyfit(x_masked, y_masked, **kwargs,
                               w = 1 / np.sqrt(variance_masked))
            model = np.poly1d(coeff)
            fitted_values = model(x_masked)
            # check for outliers

            # TODO: absolute threshold
            residuals = (model(xdata) - ydata)**2 / (variance)
            outliers = residuals > threshold

            if np.any(outliers[mask]): # are there still any unmasked residuals
                mask[residuals == residuals[mask].max()] = False
            else:
                converged = True
     
    return model(xdata), mask, model


#def procvect(xdata, ydata, variance, threshold, fit_type, absolute_threshold, kwargs):
#    '''docstring'''
#    polynomial = models.Polynomial1D(degree=1)
#    fit = fitting.LevMarLSQFitter()
#    outliersRemoved_fit = fitting.FittingWithOutlierRemoval(fit, sigma_clip)

#    filtered_data, model = outliersRemoved_fit(polynomial, xdata, ydata)

#    return model(xdata), None, model



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
