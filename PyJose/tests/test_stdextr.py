import unittest
import numpy as np
import numpy.testing as npt

from stdextr import stdextr

class test_stdextr(unittest.TestCase):
    def test_IDLOracle_regression1(self):
        x1 = np.loadtxt('tests/testData/stdextrData/x1.csv', delimiter=',')
        x2 = np.loadtxt('tests/testData/stdextrData/x2.csv', delimiter=',')
        dataim = np.loadtxt('tests/testData/stdextrData/dataim.csv', delimiter=',')
        stdspec = np.loadtxt('tests/testData/stdextrData/stdspec.csv', delimiter=',')
        stdvar = np.loadtxt('tests/testData/stdextrData/stdvar.csv', delimiter=',')
        varim = np.loadtxt('tests/testData/stdextrData/varim.csv', delimiter=',')
        x1 = int(np.asscalar(x1))
        x2 = int(np.asscalar(x2)) + 1

        output_spectrum, output_var = stdextr(dataim, varim, (x1, x2))

        npt.assert_allclose(output_spectrum, stdspec, rtol=0.1)
        npt.assert_allclose(output_var, stdvar, rtol=0.1)

if __name__ == '__main__':
    unittest.main()
