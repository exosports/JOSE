import numpy as np
import logging

def procvect(xdata, ydata, variance, threshold, fit_type, absolute_threshold, kwargs):
    '''docstring'''

    if fit_type == 'polynomial':
        coeff = np.polyfit(xdata, ydata, **kwargs)
        model = np.poly1d(coeff)

    

    return model(xdata), model
