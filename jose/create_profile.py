import numpy as np

from .procvect import procvect

def create_profile(sky_subtracted, variance, sigthresh):
    f = np.sum(sky_subtracted, axis=1, keepdims=True)
    profile_estimate = (sky_subtracted) / f
    profile = np.zeros(np.shape(sky_subtracted))
    
    # TODO: other methods of profile fitting
    x_values = np.array(list(range(len(profile_estimate[:,0]))))
    for i in range(np.shape(profile_estimate)[1]):
        profile[:, i], mask, model = procvect(x_values,
                                              sky_subtracted[:, i],
                                              variance[:, i], sigthresh,
                                              "polynomial", False,
                                              {'deg' : 3})

    # enforce positivity
    profile[profile < 0] = 0

    # normalize
    row_totals = profile.sum(axis=1, keepdims=True)
    profile = profile / row_totals

    return profile
