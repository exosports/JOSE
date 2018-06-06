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

        results_vector, new_mask, model = procvect(xvals, datav[xvals.astype(int)], varv[xvals.astype(int)], thresh, 'polynomial', False, {'deg' : parm})

        npt.assert_allclose(model(np.array(range(len(bgRow)))), bgRow)
        # don't test changing variance
        # npt.assert_allclose(new_variance, maskv_output)
        npt.assert_array_equal(new_mask, maskv_output.astype(bool))

    def test_IDLOracle_1_loose(self):
        # very loose equality test
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

        results_vector, new_mask, model = procvect(xvals, datav[xvals.astype(int)], varv[xvals.astype(int)], thresh, 'polynomial', False, {'deg' : parm})

        npt.assert_allclose(model(np.array(range(len(bgRow)))), bgRow, atol=1)
        # don't test changing variance
        # npt.assert_allclose(new_variance, maskv_output)
        # npt.assert_array_equal(new_mask, maskv_output.astype(bool))

    def test_basicFit(self):
        xvals = np.linspace(4, 10, num = 100)
        xvals_clipped = xvals[np.r_[:30, -30:0]] #cut out the middle to represent removing object spectrum
        func = lambda x: x ** 2 - x 
        yvals = func(xvals)
        yvals_clipped = func(xvals_clipped)
        variance = np.ones(np.shape(xvals_clipped)) # variance and threshold shouldn't matter for basic test
        threshold = 1
        fit_type = 'polynomial'
        fit_options = {'deg' : 2}

        calculated_values, _, model = procvect(xvals_clipped, yvals_clipped, variance, threshold,
                                            fit_type, False, fit_options)

        npt.assert_allclose(calculated_values, yvals_clipped)
        npt.assert_allclose(model(xvals), yvals)


    def test_fitWithOutliers(self):
        xvals = np.linspace(4, 10, num = 100)
        xvals_clipped = xvals[np.r_[:30, -30:0]] #cut out the middle to represent removing object spectrum
        func = lambda x: x ** 2 - x 
        yvals = func(xvals)
        yvals_clipped = func(xvals_clipped)
        variance = np.ones(np.shape(xvals_clipped)) # variance and threshold shouldn't matter for basic test
        threshold = 16
        fit_type = 'polynomial'
        fit_options = {'deg' : 2}
        yvals_withOutliers = np.copy(yvals_clipped)
        yvals_withOutliers[3] *= 10
        yvals_withOutliers[40] *= 10
        yvals_withOutliers[50] *= 10

        calculated_values, _, model = procvect(xvals_clipped, yvals_withOutliers, variance, threshold,
                                            fit_type, False, fit_options)

        npt.assert_allclose(calculated_values, yvals_clipped)
        npt.assert_allclose(model(xvals), yvals)

if __name__ == '__main__':
    unittest.main()
