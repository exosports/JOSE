import numpy as np
import logging

# TODO: change to import jose
from .fit_background import fit_background
from .stdextr import stdextr
from .create_profile import create_profile
from .extract import extract

log = logging.getLogger(__name__)

def optimal_extraction(data, variance, rn, Q, object_bounds):
    '''docstring'''
    # TODO: make function wrapper for Extraction object which only
    # returns basic answer, and possibly the object
    background = fit_background(data, object_bounds, variance)

    sky_subtracted = data - background

    #TODO: implement user-supplied mask
    standard_spectrum, var = stdextr(data, variance, object_bounds) 

    profile = create_profile(data - background, variance)

    #TODO: make sure broadcasting in correct direction
    revised_variance = rn**2 + np.abs(standard_spectrum*profile + background) \
                       / Q 

    optimal_spectrum = extract(sky_subtracted, revised_variance,
                               profile, object_bounds)
    
    return optimal_spectrum
