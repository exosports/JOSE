import unittest
import numpy as np
import numpy.testing as npt
import os
import sys

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'stdextrData')

class test_stdextr(unittest.TestCase):
    def test_IDLOracle_regression1(self):
        x1 = np.loadtxt(os.path.join(testData_directory, "x1.csv"), delimiter=',')
        x2 = np.loadtxt(os.path.join(testData_directory, "x2.csv"), delimiter=',')
        dataim = np.loadtxt(os.path.join(testData_directory, "dataim.csv"), delimiter=',')
        stdspec = np.loadtxt(os.path.join(testData_directory, "stdspec.csv"), delimiter=',')
        stdvar = np.loadtxt(os.path.join(testData_directory, "stdvar.csv"), delimiter=',')
        varim = np.loadtxt(os.path.join(testData_directory, "varim.csv"), delimiter=',')
        x1 = int(np.asscalar(x1))
        x2 = int(np.asscalar(x2)) + 1 #IDL is inclusive in the last index, numpy/python is not

        print(dir(jose))

        output_spectrum, output_var = jose.stdextr(dataim, varim, (x1, x2))

        npt.assert_allclose(output_spectrum, stdspec, rtol=0.1)
        npt.assert_allclose(output_var, stdvar, rtol=0.1)

if __name__ == '__main__':
    unittest.main()
