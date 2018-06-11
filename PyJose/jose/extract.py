import numpy as np

def extract(sky_subtracted, revised_variance, profile):
    threshold = 25
    mask = np.full(np.shape(sky_subtracted), True) #initialize to all good pixels
    converged = False
    maximum_rejects = 1
    previous_bad_pixels = np.full(np.shape(sky_subtracted), False)

    while not converged:
        denominator = np.sum(mask * profile * profile / revised_variance, axis=1)
        spectrum = np.sum(mask * profile * sky_subtracted / revised_variance, axis=1) / denominator
        
        SDR = (sky_subtracted - spectrum * profile) / revised_variance

        bad_pixels = SDR > threshold

        # flattened indexes of maximum_reject largest outliers
        largest_SDR = np.argpartition(SDR, SDR.size-maximum_rejects, axis=None)[-maximum_rejects:]

        if np.array_equal(bad_pixels, previous_bad_pixels):
            converged = True
        else:
            previous_bad_pixels = np.copy(bad_pixels)
            mask[largest_SDR // mask.shape[0], largest_SDR % mask.shape[1]] = False
            mask = np.logical_or(mask, np.logical_not(bad_pixels))

    return spectrum