import numpy as np

from .procvect import procvect

def create_profile(data, sky, variance):
    f = np.sum(data - sky, axis=1)
    profile_estimate = (data - sky) / f
    profile = np.zeros(np.shape(data))
    
    rejection_threshold = 16

    x_values = np.array(list(range(len(profile_estimate[:,0]))))
    for i in range(np.shape(profile_estimate)[1]):
        fit_complete = False
        mask = np.full(np.shape(profile_estimate[:,i]), True)
        previous_outlieres = np.full(np.shape(profile_estimate[:,i]), False)
        while not fit_complete:
            coeff = np.polyfit(x_values[mask],
                               profile_estimate[:,i][mask], 
                               deg = 3,
                               w = 1 / variance[:,i][mask])
            model = np.poly1d(coeff)

            fitted_profile = model(x_values)

            SNR = (data[:,i] - sky[:,i] - f * fitted_profile)**2 / variance[:,i]
            outliers = SNR > rejection_threshold
            if np.array_equal(previous_outlieres, outliers):
                fit_complete = True
                profile[:,i] = fitted_profile
            else:
                previous_outlieres = np.copy(outliers)
                mask[outliers] = False

    # enforce positivity
    profile[profile < 0] = 0

    # normalize
    row_totals = profile.sum(axis=1, keepdims=True)
    profile = profile / row_totals

    return profile
