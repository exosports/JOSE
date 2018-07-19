import unittest
import numpy as np
import numpy.testing as npt
from astropy.io import fits as pyfits
import os

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'fitprofData')

class test_fitprof(unittest.TestCase):
    def test_IDL_example1(self):
        dataDir = os.path.join(testData_directory, 'test_00')

        sky_background = np.loadtxt(os.path.join(dataDir, 'bgim.csv'), delimiter=',')
        data = np.loadtxt(os.path.join(dataDir, 'dataim.csv'), delimiter=',')
        variance = np.loadtxt(os.path.join(dataDir, 'varim.csv'), delimiter=',')

        profile = jose.create_profile(data, variance)

        idl_profile = np.loadtxt(os.path.join(dataDir, 'profim.csv'), delimiter=',')

        npt.assert_allclose(profile, idl_profile, rtol=1e-3, atol=0.005)


if __name__ == '__main__':
    unittest.main()
