import unittest
import numpy as np
from astropy.io import fits as pyfits
from optspecextr import optspectextr


class test_optspecextr(unittest.TestCase):
    def test_A(self):
        frame1 = pyfits.open('images/ex1.fits')[0]
        Q = frame1.header.get('EPADU')
        rn = frame1.header.get('RDNOISE') / Q

        leftBound = 240
        rightBound = 270

        varim = np.abs(frame1.data) / Q + rn**2


if __name__ == '__main__':
    unittest.main()
