import numpy as np
import matplotlib.pyplot as plt
import logging
import pickle
import types

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

        # Parse options
        if self.opt['rotate']:
            self.data = np.rot90(self.data, 3)

        self.q = self.header.get('EPADU')
        if type(self.q) == type(None):
            try:
                self.q = self.opt['EPADU']
            except KeyError:
                msg = "FITS file lacks EPADU field. Must specify in cfg."
                log.error(msg)
                raise ValueError(msg)

        self.rdnoise = self.header.get('RDNOISE')
        if type(self.rdnoise) == type(None):
            try:
                self.rdnoise = self.opt['RDNOISE']
            except KeyError:               
                msg = "FITS file lacks RDNOISE field. Must specify in cfg."
                log.error(msg)
                raise ValueError(msg)

        self.rdnoise /= self.q

        self.x1, self.x2 = self.opt['object_bounds']

        # Set up namespaces for config sections
        self.bgfit = types.SimpleNamespace()
        self.bgfit.method  = self.opt['background_fitting']['method']
        self.bgfit.thresh  = self.opt['background_fitting']['thresh']
        self.bgfit.methopt = self.opt['background_fitting']['method_options']

        self.proffit = types.SimpleNamespace()
        self.proffit.method  = self.opt['profile_fitting']['method']
        self.proffit.thresh  = self.opt['profile_fitting']['thresh']
        self.proffit.methopt = self.opt['profile_fitting']['method_options']

        self.extract = types.SimpleNamespace()
        self.extract.thresh = self.opt['extraction']['thresh']
            
    def calculate_extraction(self):
        '''
        Modifies the state of this object to calculate the 
        extraction based on the provided data
        '''         

        log.info("Calculating variance as |data| / EPADU + read_noise**2")
        self.variance = np.abs(self.data) / self.q + self.rdnoise**2

        self.background = fit_background(self.data, self.x1, self.x2,
                                         varim=self.variance)

        sky_subtracted = self.data - self.background

        #TODO: implement user-supplied mask
        standard_spectrum, var = stdextr(self.data,
                                         self.variance,
                                         self.opt['object_bounds']) 

        self.profile = create_profile(sky_subtracted, self.variance,
                                      self.opt['profile_fitting']['thresh'])

        #TODO: make sure broadcasting in correct direction
        self.revised_variance = self.rdnoise**2 + \
                                np.abs(standard_spectrum*self.profile + \
                                       self.background) / self.q

        self.optimal_spectrum = extract(sky_subtracted,
                                        self.revised_variance,
                                        self.profile,
                                        self.opt['object_bounds'],
                                        self.opt['extraction']['thresh'])
    
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


