import numpy as np

from .procvect import procvect

def create_profile(data):
    profile = np.zeros(np.shape(data))

    
    for i in range(np.shape(profile)[1]):
        profile[:,i] = procvect( list(range(len(profile[:,i]))),
                                data[:, i],

            )

    # enforce positivity
    profile[profile < 0] = 0

    # normalize
    row_totals = profile.sum(axis=1, keepdims=True)
    profile = profile / row_totals

    return profile
