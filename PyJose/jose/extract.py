import numpy as np

def extract(sky_subtracted, revised_variance, profile, standard_spectrum):
    threshold = 5
    mask = np.full(np.shape(sky_subtracted), True) #initialize to all good pixels
    converged = False
    previous_mask = np.copy(mask) # could make more effecient just by taking sum?
    maximum_rejects = 1

    while not converged:
        denominator = np.sum(mask * profile * profile / revised_variance, axis=1)
        spectrum = np.sum(mask * profile * sky_subtracted / revised_variance, axis=1) / denominator
        
        SDR = (sky_subtracted - spectrum * profile) / revised_variance


    
    mask = (sky_subtracted - standard_spectrum * profile)**2 <= revised_variance * threshold**2





    return None