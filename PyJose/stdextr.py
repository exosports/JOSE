import numpy as np


def stdextr(data, variance, object_bounds, mask = None):
    '''docstring'''

    if mask == None:
        mask = np.full(np.shape(data), True) #if no mask specified treat every pixel as a good pixel

    spectrum = np.sum( (data * mask)[:, object_bounds[0]:object_bounds[1]], 1)
    variance_estimate = np.sum( (variance * mask)[:, object_bounds[0]:object_bounds[1]], 1)

    return spectrum, variance_estimate

