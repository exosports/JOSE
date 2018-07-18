import unittest
import numpy as np
import numpy.testing as npt
import os

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'extrspecData')


class test_extrspec(unittest.TestCase):
    def test_IDLAgreement_example1(self):
        dir = os.path.join(testData_directory, 'test_00')
        sky = np.loadtxt(os.path.join(dir, 'bgim.csv'), delimiter=',')
        data = np.loadtxt(os.path.join(dir, 'dataim.csv'), delimiter=',')
        variance = np.loadtxt(os.path.join(dir, 'varim.csv'), delimiter=',')
        profile = np.loadtxt(os.path.join(dir, 'profim.csv'), delimiter=',')

        spectrum = jose.extract(data-sky, variance, profile)

        idl_spectrum = np.loadtxt(os.path.join(dir, 'optspec.csv'), delimiter=',')

        npt.assert_allclose(spectrum, idl_spectrum, rtol=1e-3, atol=0.5)

if __name__ == '__main__':
    unittest.main()
