import numpy as np

def extract(sky_subtracted, revised_variance, profile, object_bounds):
    '''docstring'''
    #TODO: implement variance from sky image
    threshold = 25
    mask = np.full(np.shape(sky_subtracted), True) #initialize to all good pixels
    mask[:, 0:object_bounds[0]] = False
    mask[:, object_bounds[1]:-1] = False
    spectrum = np.zeros(np.shape(sky_subtracted)[1])

    for i in range(sky_subtracted.shape[0]):
        converged = False
        maximum_rejects = 1
        previous_bad_pixels = np.full(np.shape(sky_subtracted[i,:]), False)

        while not converged:
            denominator = np.sum(mask[i,:] * profile[i,:] * profile[i,:] /
                                 revised_variance[i,:])
            spectrum_estimate = np.sum(mask[i,:] * profile[i,:] *
                                       sky_subtracted[i,:] /
                                       revised_variance[i,:]) / denominator
            
            residuals = (sky_subtracted[i,:] - spectrum_estimate *
                         profile[i,:])**2 / revised_variance[i,:]

            bad_pixels = residuals > threshold

            if np.array_equal(bad_pixels, previous_bad_pixels):
                converged = True
                spectrum[i] = spectrum_estimate
            else:
                previous_bad_pixels = np.copy(bad_pixels)
                mask[i, residuals == residuals[mask[i,:]].max()] = False

    return spectrum
