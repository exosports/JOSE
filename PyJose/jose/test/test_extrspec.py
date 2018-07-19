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
        data_skySubtracted = np.loadtxt(os.path.join(dir, 'dataim.csv'), delimiter=',')
        variance = np.loadtxt(os.path.join(dir, 'varim.csv'), delimiter=',')
        profile = np.loadtxt(os.path.join(dir, 'profim.csv'), delimiter=',')
        left_bound = int(np.asscalar(np.loadtxt(os.path.join(dir, 'x1.csv'))))
        right_bound = int(np.asscalar(np.loadtxt(os.path.join(dir, 'x2.csv'))))

        spectrum = jose.extract(data_skySubtracted, variance, profile, (left_bound, right_bound))

        idl_spectrum = np.loadtxt(os.path.join(dir, 'optspec.csv'), delimiter=',')

        npt.assert_allclose(spectrum, idl_spectrum, rtol=1e-2, atol=1)

if __name__ == '__main__':
    unittest.main()
