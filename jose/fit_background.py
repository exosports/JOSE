import numpy as np
import logging
import matplotlib.pyplot as plt

from .procvect import procvect

log = logging.getLogger(__name__)

def fit_background(data, x1, x2, bgdeg=1, bgmask=None,
                   bgres=None, bpct=None, bthresh=3, errvect=None,
                   gotovect=None, inmask=None, nobgfit=None, plottype=None,
                   q=None, skyvar=None, varim=None, verbose=None, v0=None):
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
    log.info("Calculating background by linearly interpolating " + \
             "excluding spectrum from " + str(x1) + " to " + str(x2))

    if type(varim) == type(None): varim = np.ones(data.shape)

    # set up mask which excludes object between x1 and x2
    object_mask = np.full(np.shape(data)[1], False)
    object_mask[:x1] = True
    object_mask[x2:] = True

    ny, nx = data.shape

    x_values = np.array(range(np.shape(data)[1]))

    bg = np.zeros(data.shape)
    
    ray_mask = np.full(data.shape, True) # initially no pixels are masked

    #wavelength stores in rows, iterate over each
    for wavelength in range(len(data)): 
        # for each wavelength use a low order polynomial to
        # figure the background image

        out = procvect(xdata = x_values[object_mask], 
                       ydata = data[wavelength,:][object_mask],
                       variance = varim[wavelength, :][object_mask],
                       threshold = bthresh,
                       fit_type = "polynomial",
                       absolute_threshold = False,
                       kwargs = {'deg' : bgdeg})

        _, outlier_mask, model = out

        #use fitted model to make background image
        bg[wavelength, :] = model(x_values) 
        ray_mask[wavelength, :][object_mask] = outlier_mask

    return bg
