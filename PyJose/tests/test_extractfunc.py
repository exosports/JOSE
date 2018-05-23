import unittest
import numpy as np
import numpy.testing as npt

from extractfunc import extractfunc

class test_extractfunc(unittest.TestCase):
    def test_IDLAgreement1(self):
        coeffv = np.loadtxt('tests/testData/extractfuncData/coeffv.csv', delimiter=',')
        datav = np.loadtxt('tests/testData/extractfuncData/datav.csv', delimiter=',')
        eval = np.loadtxt('tests/testData/extractfuncData/eval.csv', delimiter=',')
        opt = np.loadtxt('tests/testData/extractfuncData/opt.csv', delimiter=',')
        opvar = np.loadtxt('tests/testData/extractfuncData/opvar.csv', delimiter=',')
        profv = np.loadtxt('tests/testData/extractfuncData/profv.csv', delimiter=',')
        varv = np.loadtxt('tests/testData/extractfuncData/varv.csv', delimiter=',')
        xvals = np.loadtxt('tests/testData/extractfuncData/xvals.csv', delimiter=',')

        results, opvarResult = extractfunc(xvals, datav, varv, profv, eval, coeffv)

        npt.assert_allclose(results, opt)

    def test_allBad(self):
        xvals = np.array([1,2,3])

        datav = np.linspace(0, 10)
        varv = np.linspace(0, 10)
        profv = np.zeros(size(varv)) #all bad pixels
        eval = None
        coeffv = None


        results = extractfunc(xvals, datav, varv, profv, eval, coeffv, )

if __name__ == '__main__':
    unittest.main()
