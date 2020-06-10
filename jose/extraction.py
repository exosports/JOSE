import numpy as np
import matplotlib.pyplot as plt
import logging
import pickle

from .fit_background import fit_background
from .stdextr import stdextr
from .create_profile import create_profile
from .extract import extract

log = logging.getLogger(__name__)


class Extraction(object):
    """
    Responsible for tracking data from one extraction and 
    producing appropriate figures
    """
    
    def __init__(self, hdu, opt):
        """
        Initialize Extraction object.

        Arguments
        ---------
        hdu: astropy HDU object
            HDU object containing a single data frame and header.

        opt: dict
            Dictionary of configuration options
        """
        

        self.opt    = opt
        self.data   = hdu.data
        self.header = hdu.header

        # Rotate image 90 deg clockwise (wavelength ascending left to
        # right becomes top to bottom)
        if self.opt['rotate']:
            self.data = np.rot90(self.data, 3)
                
    def calculate_extraction(self, options):
        '''
        Modifies the state of this object to calculate the 
        extraction based on the provided data
        '''
        
        log.info("Getting electrons per data number and read noise " + 
                 "from FITS file")
        Q = self.header.get('EPADU')
        if Q == None:
            try:
                Q = options['EPADU']
            except KeyError:
                msg = "FITS file lacks EPADU field. Must specify in cfg."
                log.error(msg)
                raise ValueError(msg)            

        raw_read_noise = self.header.get('RDNOISE')
        if raw_read_noise == None:
            try:
                raw_read_noise = options['RDNOISE']
            except KeyError:               
                msg = "FITS file lacks RDNOISE field. Must specify in cfg."
                log.error(msg)
                raise ValueError(msg)

        read_noise = raw_read_noise / Q

        log.info("Calculating variance as |data| / EPADU + read_noise**2")
        self.variance = np.abs(self.data) / Q + read_noise**2

        self.background = fit_background(self.data,
                                         options['object_bounds'],
                                         self.variance)

        sky_subtracted = self.data - self.background

        #TODO: implement user-supplied mask
        standard_spectrum, var = stdextr(self.data,
                                         self.variance,
                                         options['object_bounds']) 

        self.profile = create_profile(sky_subtracted, self.variance)

        #TODO: make sure broadcasting in correct direction
        self.revised_variance = read_noise**2 + \
                                np.abs(standard_spectrum*self.profile + \
                                       self.background) / Q 

        self.optimal_spectrum = extract(sky_subtracted,
                                        self.revised_variance,
                                        self.profile,
                                        options['object_bounds'])
    
    def make_spectrum_figure(self):
        r'''Returns figure and axes object for extracted spectrum'''
        f, ax = plt.subplots()
        ax.plot(self.optimal_spectrum)
        return f, ax

    def save(self, fname):
        """
        Save object to file.
        """
        with open(fname, 'wb') as f:
            pickle.dump(self, f)

def load(fname):
    """
    Load Extraction object from file.
    """
    with open(fname, 'rb') as f:
        extract = pickle.load(f)

    return extract


