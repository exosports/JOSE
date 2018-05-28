import unittest
import numpy as np
import numpy.testing as npt

from procvect import procvect

class test_procvect(unittest.TestCase):
    def test_IDLOracle_1(self):
        # TODO: find way to automate these for all test data
        bcrv = np.loadtxt('tests/testData/procvectData/test_00/bcrv.csv', delimiter=',')
        bgRow = np.loadtxt('tests/testData/procvectData/test_00/bgRow.csv', delimiter=',')
        bpct = np.loadtxt('tests/testData/procvectData/test_00/bpct.csv', delimiter=',')
        bthresh = np.loadtxt('tests/testData/procvectData/test_00/bthresh.csv', delimiter=',')
        crv = np.loadtxt('tests/testData/procvectData/test_00/crv.csv', delimiter=',')
        datav = np.loadtxt('tests/testData/procvectData/test_00/datav.csv', delimiter=',')
        errflag = np.loadtxt('tests/testData/procvectData/test_00/errflag.csv', delimiter=',')
        fiteval = np.loadtxt('tests/testData/procvectData/test_00/fiteval.csv', delimiter=',')
        func = 'polyfunc' #TODO: load from file or check? 
        i = np.loadtxt('tests/testData/procvectData/test_00/i.csv', delimiter=',')
        maskv = np.loadtxt('tests/testData/procvectData/test_00/maskv.csv', delimiter=',')
        maskv_output = np.loadtxt('tests/testData/procvectData/test_00/maskv_output.csv', delimiter=',')
        parm = np.loadtxt('tests/testData/procvectData/test_00/parm.csv', delimiter=',')
        plottype = np.loadtxt('tests/testData/procvectData/test_00/plottype.csv', delimiter=',')
        q = np.loadtxt('tests/testData/procvectData/test_00/q.csv', delimiter=',')
        skyvarv = np.loadtxt('tests/testData/procvectData/test_00/skyvarv.csv', delimiter=',')
        thresh = np.loadtxt('tests/testData/procvectData/test_00/thresh.csv', delimiter=',')
        v0 = np.loadtxt('tests/testData/procvectData/test_00/v0.csv', delimiter=',')
        varv = np.loadtxt('tests/testData/procvectData/test_00/varv.csv', delimiter=',')
        varv_output = np.loadtxt('tests/testData/procvectData/test_00/varv_output.csv', delimiter=',')
        vectnum = np.loadtxt('tests/testData/procvectData/test_00/vectnum.csv', delimiter=',')
        verbose = np.loadtxt('tests/testData/procvectData/test_00/verbose.csv', delimiter=',')
        xvals = np.loadtxt('tests/testData/procvectData/test_00/xvals.csv', delimiter=',')

        results_vector, new_variance, new_mask = procvect()

        npt.assert_allclose(results_vector, bgRow)
        npt.assert_allclose(new_variance, maskv_output)
        npt.assert_allclose(new_mask, varv_output)

if __name__ == '__main__':
    unittest.main()
