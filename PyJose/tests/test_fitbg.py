import unittest
import numpy as np
from astropy.io import fits as pyfits


class test_fitbg(unittest.TestCase):
    def test_fitsLoading(self):
        '''Sanity check to ensure test data is present'''
        data = pyfits.getdata('images/ex1.fits') #more of an integration test than unit tests, 


if __name__ == '__main__':
    unittest.main()
