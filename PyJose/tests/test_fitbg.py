import unittest
import numpy as np
import numpy.testing as npt
from astropy.io import fits as pyfits

from fitbg import fitbg


class test_fitbg(unittest.TestCase):
    def test_testDataPresent(self):
        '''Sanity check to ensure test data is present'''
        data = pyfits.open('images/ex1.fits') #more of an integration test than unit tests, 
        dataim = np.loadtxt('tests/testData/fitbgData/dataim.csv', delimiter=',')
        x1 = np.loadtxt('tests/testData/fitbgData/x1.csv', delimiter=',')
        x2 = np.loadtxt('tests/testData/fitbgData/x2.csv', delimiter=',')
        bgdeg = np.loadtxt('tests/testData/fitbgData/bgdeg.csv', delimiter=',')
        bgmask = np.loadtxt('tests/testData/fitbgData/bgmask.csv', delimiter=',')
        bgres = np.loadtxt('tests/testData/fitbgData/bgres.csv', delimiter=',')
        bthresh = np.loadtxt('tests/testData/fitbgData/bthresh.csv', delimiter=',')
        errvect = np.loadtxt('tests/testData/fitbgData/errvect.csv', delimiter=',')
        gotovect = np.loadtxt('tests/testData/fitbgData/gotovect.csv', delimiter=',')
        inmask = np.loadtxt('tests/testData/fitbgData/inmask.csv', delimiter=',')
        plottype = np.loadtxt('tests/testData/fitbgData/plottype.csv', delimiter=',')
        q = np.loadtxt('tests/testData/fitbgData/q.csv', delimiter=',')
        skyvar = np.loadtxt('tests/testData/fitbgData/skyvar.csv', delimiter=',')
        varim = np.loadtxt('tests/testData/fitbgData/varim.csv', delimiter=',')
        verbose = np.loadtxt('tests/testData/fitbgData/verbose.csv', delimiter=',')
        v0 = np.loadtxt('tests/testData/fitbgData/v0.csv', delimiter=',')

    def test_testIDLAgreement_fitbg_loose(self):
        '''Recorded data from first part of IDL jose tutorial to compare against'''
        data = pyfits.open('images/ex1.fits') #more of an integration test than unit tests, 
        dataim = np.loadtxt('tests/testData/fitbgData/dataim.csv', delimiter=',')
        x1 = np.loadtxt('tests/testData/fitbgData/x1.csv', delimiter=',')
        x2 = np.loadtxt('tests/testData/fitbgData/x2.csv', delimiter=',')
        # bgdeg = polynomial_degree = what degree of polynomial to use to fit across data
        bgdeg = np.loadtxt('tests/testData/fitbgData/bgdeg.csv', delimiter=',')
        bgmask = np.loadtxt('tests/testData/fitbgData/bgmask.csv', delimiter=',')
        bgres = np.loadtxt('tests/testData/fitbgData/bgres.csv', delimiter=',')
        bthresh = np.loadtxt('tests/testData/fitbgData/bthresh.csv', delimiter=',')
        errvect = np.loadtxt('tests/testData/fitbgData/errvect.csv', delimiter=',')
        gotovect = np.loadtxt('tests/testData/fitbgData/gotovect.csv', delimiter=',')
        inmask = np.loadtxt('tests/testData/fitbgData/inmask.csv', delimiter=',')
        plottype = np.loadtxt('tests/testData/fitbgData/plottype.csv', delimiter=',')
        q = np.loadtxt('tests/testData/fitbgData/q.csv', delimiter=',')
        skyvar = np.loadtxt('tests/testData/fitbgData/skyvar.csv', delimiter=',')
        varim = np.loadtxt('tests/testData/fitbgData/varim.csv', delimiter=',')
        verbose = np.loadtxt('tests/testData/fitbgData/verbose.csv', delimiter=',')
        v0 = np.loadtxt('tests/testData/fitbgData/v0.csv', delimiter=',')

        bpct = None
        nobgfit = None

        results = fitbg(dataim, (int(np.asscalar(x1)), int(np.asscalar(x2))), varim)

        bgim = np.loadtxt('tests/testData/fitbgData/bgim.csv', delimiter=',')

        npt.assert_allclose(results, bgim, rtol=0.01)



    def test_flatBackground(self):
        data = np.zeros((200,200))
        variance = np.ones(np.shape(data))
        object_bounds = (80, 120)

        background_image = fitbg(data, object_bounds, variance)

        npt.assert_allclose(background_image, np.zeros(np.shape(data)))

    def test_flatBackgroundWithObject(self):
        data = np.ones((200,200))
        data[:, 90:110] = 100
        variance = np.ones(np.shape(data))
        object_bounds = (80, 120)

        background_image = fitbg(data, object_bounds, variance)

        npt.assert_allclose(background_image, np.ones(np.shape(data)))


if __name__ == '__main__':
    unittest.main()
