import numpy as np
import matplotlib.pyplot as plt
import logging

from fit_background import fit_background
from stdextr import stdextr
from create_profile import create_profile
from extract import extract

log = logging.getLogger(__name__)


class Extraction(object):
    """Responsible for tracking data from one extraction and producing appropriate figures and stuff"""
    
    def __init__(self, dataFits):
        self.dataFits = dataFits

    def calculate_extraction(self, options):
        '''Modifies the state of this object to calculate the extraction based on the provided data'''
        
        log.info("Getting electrons per data number and read noise from FITS file")
        Q = self.dataFits.header.get('EPADU')
        if Q == None:
            #TODO: should this include print statement?
            message = 'FITS header lacks EPADU field, modify file or specify in config' #TODO: actually use value from config
            log.error(message)
            raise ValueError(message)

        raw_read_noise = self.dataFits.header.get('RDNOISE')
        if raw_read_noise == None:
            message = 'FITS header lacks RDNOISE field, modify file or specify in config'
            log.error(message)
            raise ValueError(message)

        read_noise = raw_read_noise / Q

        log.info("Calculating variance as |data| / EPADU + read_noise**2")
        self.variance = np.abs(self.dataFits.data) / Q + read_noise**2

        self.background = fit_background(self.dataFits.data, options['object_bounds'], self.variance)

        sky_subtracted = self.dataFits.data - self.background

        standard_spectrum, var = stdextr(self.dataFits.data, self.variance, options['object_bounds']) #TODO: implement user-supplied mask

        self.profile = create_profile(sky_subtracted, self.variance)

        self.revised_variance = read_noise**2 + np.abs(standard_spectrum*self.profile + self.background) / Q #TODO: make sure broadcasting in correct direction

        self.optimal_spectrum = extract(sky_subtracted, self.revised_variance, self.profile, options['object_bounds'])
    

    def make_spectrum_figure(self):
        r'''Returns figure and axes object for extracted spectrum'''
        f, ax = plt.subplots()
        ax.plot(self.optimal_spectrum)
        return f, ax





