import numpy as np


def stdextr(data, variance, bounds, mask = None):
    '''docstring'''

    if mask == None:
        #if no mask specified treat every pixel as a good pixel
        mask = np.full(np.shape(data), True) 

    spectrum = np.sum( (data * mask)[:, bounds[0]:bounds[1]], 1, keepdims=True)
    variance_estimate = np.sum( (variance * mask)[:, bounds[0]:bounds[1]], 1,
                                keepdims=True)

    return spectrum, variance_estimate

