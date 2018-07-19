import unittest
import numpy as np
import numpy.testing as npt

import jose

class test_create_profile(unittest.TestCase):
    def test_positivity(self):
        data = np.ones((200,200))
        data[0,0] = -1
        variance = np.ones(data.shape) / 100

        profile = jose.create_profile(data, variance)

        self.assertTrue(np.all(profile >= 0))

    def test_normalization(self):
        data = np.ones((200,200))
        variance = np.ones(data.shape) / 100

        profile = jose.create_profile(data, variance)

        npt.assert_allclose(np.sum(profile, axis=1), 1.0)



if __name__ == '__main__':
    unittest.main()
