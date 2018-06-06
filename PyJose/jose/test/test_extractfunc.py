import unittest
import numpy as np
import numpy.testing as npt
import os

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'extractfuncData')

class test_extractfunc(unittest.TestCase):
    def test_IDLAgreement1(self):
        coeffv = np.loadtxt(os.path.join(testData_directory, "coeffv.csv"), delimiter=',')
        datav = np.loadtxt(os.path.join(testData_directory, "datav.csv"), delimiter=',')
        eval = np.loadtxt(os.path.join(testData_directory, "eval.csv"), delimiter=',')
        opt = np.loadtxt(os.path.join(testData_directory, "opt.csv"), delimiter=',')
        opvar = np.loadtxt(os.path.join(testData_directory, "opvar.csv"), delimiter=',')
        profv = np.loadtxt(os.path.join(testData_directory, "profv.csv"), delimiter=',')
        varv = np.loadtxt(os.path.join(testData_directory, "varv.csv"), delimiter=',')
        xvals = np.loadtxt(os.path.join(testData_directory, "xvals.csv"), delimiter=',')

        results, opvarResult = jose.extractfunc(xvals, datav, varv, profv, eval, coeffv)

        npt.assert_allclose(results, opt)

    def test_allBad(self):
        xvals = np.array([1,2,3])

        datav = np.linspace(0, 10)
        varv = np.linspace(0, 10)
        profv = np.zeros(np.shape(varv)) #all bad pixels
        eval = None
        coeffv = None


        result, opvarResult = jose.extractfunc(xvals, datav, varv, profv, eval, coeffv)

        self.assertEqual(result, 0)
        self.assertEqual(opvarResult, None)


if __name__ == '__main__':
    unittest.main()
