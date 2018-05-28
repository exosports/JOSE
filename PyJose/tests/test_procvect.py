import unittest
import numpy as np
import numpy.testing as npt

class test_procvect(unittest.TestCase):
    def test_IDLOracle_1(self):
        # TODO: find way to automate these for all test data
        bcrv = np.loadtxt('tests/testData/procvectData/bcrv.csv', delimiter=',')
        bgRow = np.loadtxt('tests/testData/procvectData/bgRow.csv', delimiter=',')
        bpct = np.loadtxt('tests/testData/procvectData/bpct.csv', delimiter=',')
        bthresh = np.loadtxt('tests/testData/procvectData/bthresh.csv', delimiter=',')
        crv = np.loadtxt('tests/testData/procvectData/crv.csv', delimiter=',')
        datav = np.loadtxt('tests/testData/procvectData/datav.csv', delimiter=',')
        errflab = np.loadtxt('tests/testData/procvectData/errflab.csv', delimiter=',')
        fiteval = np.loadtxt('tests/testData/procvectData/fiteval.csv', delimiter=',')
        func = 'polyfunc' #TODO: load from file or check? 
        i = np.loadtxt('tests/testData/procvectData/i.csv', delimiter=',')
        maskv = np.loadtxt('tests/testData/procvectData/maskv.csv', delimiter=',')
        maskv_output = np.loadtxt('tests/testData/procvectData/maskv_output.csv', delimiter=',')
        parm = np.loadtxt('tests/testData/procvectData/parm.csv', delimiter=',')
        plottype = np.loadtxt('tests/testData/procvectData/plottype.csv', delimiter=',')
        q = np.loadtxt('tests/testData/procvectData/q.csv', delimiter=',')
        skyvarv = np.loadtxt('tests/testData/procvectData/skyvarv.csv', delimiter=',')
        thresh = np.loadtxt('tests/testData/procvectData/thresh.csv', delimiter=',')
        v0 = np.loadtxt('tests/testData/procvectData/v0.csv', delimiter=',')
        varv = np.loadtxt('tests/testData/procvectData/varv.csv', delimiter=',')
        varv_output = np.loadtxt('tests/testData/procvectData/varv_output.csv', delimiter=',')
        vectnum = np.loadtxt('tests/testData/procvectData/vectnum.csv', delimiter=',')
        verbose = np.loadtxt('tests/testData/procvectData/verbose.csv', delimiter=',')
        xvals = np.loadtxt('tests/testData/procvectData/xvals.csv', delimiter=',')



if __name__ == '__main__':
    unittest.main()
