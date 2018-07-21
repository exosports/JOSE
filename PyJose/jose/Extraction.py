import numpy as np
import logging

log = logging.getLogger(__name__)


class Extraction(object):
    """Responsible for tracking data from one extraction and producing appropriate figures and stuff"""
    
    def __init__(self, dataFits):
        self.dataFits = dataFits

    def calculate_extraction(self, options):
        '''Modifies the state of this object to calculate the extraction based on the provided data'''
        
        log.info("Getting electrons per data number and read noise from FITS file")
        Q = frame1.header.get('EPADU')
        if Q == None:
            message = 'FITS header lacks EPADU field, modify file or specify in config'
            log.error(message)
            raise ValueError(message)

        raw_read_noise = self.dataFits.header.get('RDNOISE')
        if raw_read_noise == None:
            message = 'FITS header lacks RDNOISE field, modify file or specify in config'
            log.error(message)
            raise ValueError(message)

        read_noise = raw_read_noise / Q


        log.info("Calculating variance as |data| / EPADU + read_noise**2")
        self.variance = np.abs(dataFits.data) / Q + read_noise**2



