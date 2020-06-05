import logging
import numpy as np

# should these low level functions be done in C for performance?

log = logging.getLogger(__name__)

def extractfunc(xvals, datav, varv, profv, eval, coeffv):
    '''docstring'''

    #TODO: input validation with logging

    goodPixels = profv != 0
    if not np.any(goodPixels): #all pixels are bad
        log.error('No good pixels in data, returning 0')
        return 0, None
    
    denominator = np.sum( profv[goodPixels] * profv[goodPixels] /
                          varv[goodPixels]) #avoid recalculation
    optimalSpectrum = np.sum( profv[goodPixels] * datav[goodPixels] /
                              varv[goodPixels]) / denominator
    spectrumVariance = np.sum(profv[goodPixels]) / denominator 

    return optimalSpectrum, spectrumVariance


