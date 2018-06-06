import unittest
import numpy as np
import numpy.testing as npt
from astropy.io import fits as pyfits
import os

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'optspecextrData')

class test_optspecextr(unittest.TestCase):
    def test_fullIntegration_example1(self):
        example1dir = os.path.join(testData_directory, "example1")
        frame1 = pyfits.open(os.path.join(example1dir, 'ex1.fits'))[0]
        Q = frame1.header.get('EPADU')
        rn = frame1.header.get('RDNOISE') / Q

        leftBound = 240
        rightBound = 270

        varim = np.abs(frame1.data) / Q + rn**2

        optimal_spectrum = jose.optspectextr()

        opspec1 = np.loadtxt(os.path.join(example1dir, 'opspec1.csv'), delimiter=',')

        npt.assert_allclose(optimal_spectrum, opspec1)



if __name__ == '__main__':
    unittest.main()
