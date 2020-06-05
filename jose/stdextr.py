import numpy as np


def stdextr(data, variance, bounds, mask = None):
    '''docstring'''

    if mask == None:
        #if no mask specified treat every pixel as a good pixel
        mask = np.full(np.shape(data), True) 

    spectrum = np.sum( (data * mask)[:, bounds[0]:bounds[1]], 1)
    variance_estimate = np.sum( (variance * mask)[:, bounds[0]:bounds[1]], 1)

    return spectrum, variance_estimate

