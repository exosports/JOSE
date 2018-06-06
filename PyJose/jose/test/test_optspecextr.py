import unittest
import numpy as np
import numpy.testing as npt
from astropy.io import fits as pyfits
from optspecextr import optspectextr


class test_optspecextr(unittest.TestCase):
    def test_fullIntegration_example1(self):
        frame1 = pyfits.open('tests/testData/optspecextr/example1/ex1.fits')[0]
        Q = frame1.header.get('EPADU')
        rn = frame1.header.get('RDNOISE') / Q

        leftBound = 240
        rightBound = 270

        varim = np.abs(frame1.data) / Q + rn**2

        optimal_spectrum = optspectextr()

        opspec1 = np.loadtxt('tests/testData/optspecextr/example1/opspec1.csv', delimiter=',')

        npt.assert_allclose(optimal_spectrum, opspec1)



if __name__ == '__main__':
    unittest.main()
