import numpy as np
import logging

from .procvect import procvect

log = logging.getLogger(__name__)

def fit_background(data, object_bounds, variance):
    '''Determine the background of the image.
    
    Arguments
    ---------
    data: array
        Spectral image array.

    object_bounds: 2-item list
        Region (in x dimension) excluded from background calculation 
        (the spectrum)

    variance: array
        Variance array corresponding to data

    Returns
    -------
    background_image: array
        Background array.

'''
    log.info('Calculating background by linearly interpolating excluding object at '
             + str(object_bounds))

    # set up mask which excludes object between x1 and x2
    object_mask = np.full(np.shape(data)[0], False)
    object_mask[:object_bounds[0]] = True
    object_mask[object_bounds[1]:] = True

    x_values = np.array(range(np.shape(data)[1]))

    background_image = np.zeros(np.shape(data))
    ray_mask = np.full(np.shape(data), True) # initially no pixels are masked

    for wavelength in range(len(data)): #wavelenght stores in rows, iterate over each
        # for each wavelength use a low order polynomial to figure the background image

        _, outlier_mask, model = procvect(xdata = x_values[object_mask], 
                                          ydata = data[wavelength,:][object_mask],
                                          variance = variance[wavelength, :][object_mask],
                                          threshold = 9,
                                          fit_type = "polynomial",
                                          absolute_threshold = False,
                                          kwargs = {'deg' : 1})
       
        background_image[wavelength, :] = model(x_values) #use fitted model to make background image
        ray_mask[wavelength, :][object_mask] = outlier_mask


    return background_image
