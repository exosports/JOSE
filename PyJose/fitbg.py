import numpy as np


def fitbg(dataImage, x1, x2,):
    dims = size(dataim)
    nx = dims[1]
    ny = dims[2]

    bgdeg = 1
    backgroundThreshold = 3
    verbosityLevel = 0
    plotType = [0,0,0,0]
    gotovect = -1 #maybe replace with NONE
    inmask = np.zeros(())