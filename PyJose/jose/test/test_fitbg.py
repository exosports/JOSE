import unittest
import numpy as np
import numpy.testing as npt
from astropy.io import fits as pyfits
import os

import jose

testData_directory = os.path.join(os.path.dirname(__file__), 'testData', 'fitbgData', 'test_00')

class test_fit_background(unittest.TestCase):
    def test_testDataPresent(self):
        '''Sanity check to ensure test data is present'''
        dataim = np.loadtxt(os.path.join(testData_directory, "dataim.csv"), delimiter=',')
        x1 = np.loadtxt(os.path.join(testData_directory, "x1.csv"), delimiter=',')
        x2 = np.loadtxt(os.path.join(testData_directory, "x2.csv"), delimiter=',')
        bgdeg = np.loadtxt(os.path.join(testData_directory, "bgdeg.csv"), delimiter=',')
        bgmask = np.loadtxt(os.path.join(testData_directory, "bgmask.csv"), delimiter=',')
        bgres = np.loadtxt(os.path.join(testData_directory, "bgres.csv"), delimiter=',')
        bthresh = np.loadtxt(os.path.join(testData_directory, "bthresh.csv"), delimiter=',')
        errvect = np.loadtxt(os.path.join(testData_directory, "errvect.csv"), delimiter=',')
        gotovect = np.loadtxt(os.path.join(testData_directory, "gotovect.csv"), delimiter=',')
        inmask = np.loadtxt(os.path.join(testData_directory, "inmask.csv"), delimiter=',')
        plottype = np.loadtxt(os.path.join(testData_directory, "plottype.csv"), delimiter=',')
        q = np.loadtxt(os.path.join(testData_directory, "q.csv"), delimiter=',')
        skyvar = np.loadtxt(os.path.join(testData_directory, "skyvar.csv"), delimiter=',')
        varim = np.loadtxt(os.path.join(testData_directory, "varim.csv"), delimiter=',')
        verbose = np.loadtxt(os.path.join(testData_directory, "verbose.csv"), delimiter=',')
        v0 = np.loadtxt(os.path.join(testData_directory, "v0.csv"), delimiter=',')


    def test_testIDLAgreement_fit_background_loose(self):
        '''Recorded data from first part of IDL jose tutorial to compare against'''
        dataim = np.loadtxt(os.path.join(testData_directory, "dataim.csv"), delimiter=',')
        x1 = np.loadtxt(os.path.join(testData_directory, "x1.csv"), delimiter=',')
        x2 = np.loadtxt(os.path.join(testData_directory, "x2.csv"), delimiter=',')
        bgdeg = np.loadtxt(os.path.join(testData_directory, "bgdeg.csv"), delimiter=',')
        bgmask = np.loadtxt(os.path.join(testData_directory, "bgmask.csv"), delimiter=',')
        bgres = np.loadtxt(os.path.join(testData_directory, "bgres.csv"), delimiter=',')
        bthresh = np.loadtxt(os.path.join(testData_directory, "bthresh.csv"), delimiter=',')
        errvect = np.loadtxt(os.path.join(testData_directory, "errvect.csv"), delimiter=',')
        gotovect = np.loadtxt(os.path.join(testData_directory, "gotovect.csv"), delimiter=',')
        inmask = np.loadtxt(os.path.join(testData_directory, "inmask.csv"), delimiter=',')
        plottype = np.loadtxt(os.path.join(testData_directory, "plottype.csv"), delimiter=',')
        q = np.loadtxt(os.path.join(testData_directory, "q.csv"), delimiter=',')
        skyvar = np.loadtxt(os.path.join(testData_directory, "skyvar.csv"), delimiter=',')
        varim = np.loadtxt(os.path.join(testData_directory, "varim.csv"), delimiter=',')
        verbose = np.loadtxt(os.path.join(testData_directory, "verbose.csv"), delimiter=',')
        v0 = np.loadtxt(os.path.join(testData_directory, "v0.csv"), delimiter=',')

        bpct = None
        nobgfit = None

        results = jose.fit_background(dataim, (int(np.asscalar(x1)), int(np.asscalar(x2))), varim)

        bgim = np.loadtxt(os.path.join(testData_directory, "bgim.csv"), delimiter=',')

        npt.assert_allclose(results, bgim, rtol=0.01)

    def test_IDLAgreement_example1(self):
        print(os.getcwd())
        imageDir = 'images'
        frame1 = pyfits.open(os.path.join(imageDir, 'ex1.fits'))[0]
        Q = frame1.header.get('EPADU')
        rn = frame1.header.get('RDNOISE') / Q
        leftBound = 240
        rightBound = 270
        varim = np.abs(frame1.data) / Q + rn**2

        background = jose.fit_background(frame1.data, (leftBound, rightBound), varim)

        example1dir = os.path.join(os.path.dirname(__file__), 'testData', 'fitbgData', 'test_01')
        idl_background = np.loadtxt(os.path.join(example1dir, 'bgim.csv'), delimiter=',')

        npt.assert_allclose(background, idl_background, rtol=1e-3, atol=0.5)



    def test_flatBackground(self):
        data = np.zeros((200,200))
        variance = np.ones(np.shape(data))
        object_bounds = (80, 120)

        background_image = jose.fit_background(data, object_bounds, variance)

        npt.assert_allclose(background_image, np.zeros(np.shape(data)))

    def test_flatBackgroundWithObject(self):
        data = np.ones((200,200))
        data[:, 90:110] = 100
        variance = np.ones(np.shape(data))
        object_bounds = (80, 120)

        background_image = jose.fit_background(data, object_bounds, variance)

        npt.assert_allclose(background_image, np.ones(np.shape(data)))


if __name__ == '__main__':
    unittest.main()
