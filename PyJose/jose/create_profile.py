import numpy as np

def create_profile(data):
    profile = np.zeros(np.shape(data))

    # enforce positivity
    profile[profile < 0] = 0

    # normalize
    row_totals = profile.sum(axis=1, keepdims=True)
    profile = profile / row_totals

    return profile
