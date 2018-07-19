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
    background = fit_background(data, object_bounds, variance)

    sky_subtracted = data - background

    standard_spectrum, var = stdextr(data, variance, object_bounds) #TODO: implement user-supplied mask

    profile = create_profile(data - background, variance)

    revised_variance = rn**2 + np.abs(standard_spectrum*profile + background) / Q #TODO: make sure broadcasting in correct direction

    optimal_spectrum = extract(sky_subtracted, revised_variance, profile)
    
    return optimal_spectrum
