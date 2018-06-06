import numpy as np
import logging

from .fitbg import fitbg
from .stdextr import stdextr
from .create_profile import create_profile

log = logging.getLogger(__name__)

def optimal_extraction(data, variance, rn, Q, object_bounds):
    '''docstring'''
    background = fitbg(data, object_bounds, variance)

    sky_subtracted = data - background

    standard_spectrum = stdextr(data, variance, object_bounds) #TODO: implement user-supplied mask

    profile = create_profile()

    return None
