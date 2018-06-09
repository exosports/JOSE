import numpy as np

def extract(sky_subtracted, revised_variance, profile, standard_spectrum):
    threshold = 5
    
    # Good pixels are True, bad pixels False
    mask = (sky_subtracted - standard_spectrum * profile)**2 <= revised_variance * threshold**2



    return None