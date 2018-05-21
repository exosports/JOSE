import numpy as np
import logging

def fitbg(dataim, x1, x2, bgdeg, bgmask, bgres, bpct, bthresh, 
          errvect, gotovect, inmask, nobgfit, plottype, q, 
          skyvar, varim, verbose, v0):
    '''docstring'''


    bgim = np.loadtxt('tests/testData/fitbgData/bgim.csv', delimiter=',')
    return bgim
