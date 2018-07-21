import numpy as np
import logging
import argparse
from astropy.io import fits as pyfits

import jose

log = logging.getLogger('jose')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    dataFits = None #get from argparser

    # this should deal with all file I/O, make calls to object to get apporpriate data then write it
    extract = jose.Extraction(dataFits)
    extract.calculate_extraction(None)

    # get output from extract and write to file depending on arguments 

    # write images, figures, data, print info to user
