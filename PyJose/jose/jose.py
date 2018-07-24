import numpy as np
import logging
import argparse
import datetime
import os
from astropy.io import fits as pyfits

from Extraction import Extraction

log = logging.getLogger('jose')

# TODO: should this copy the data?
def write_output_files(extraction, targetDir):
    r'''Writes results of extraction to `targetDir`

    Parameters
    ----------
    extraction : jose.Extraction
        Extraction object resulting from running jose
    targetDir : str
        Name of directory

    Notes
    -----
    Writes out relevant data from `extraction` object as FITS files
    and .npy Numpy files. Puts copy of configuration used under config.yaml
    and human readable summary under results.txt.
    '''
    # results.txt
    with open(os.path.join(targetDir, 'results.txt'), 'w') as results:
        results.write('test\n') #TODO: make human readable output

def write_figures(extraction, targetDir):
    r'''docstrng'''
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    # object bounds need to be supplied by the user
    # require output directory
    dataFits = None #get from argparser
    baseDir = os.path.join(os.getcwd(), 'outputTests') #TODO: parse from command line

    # this should deal with all file I/O, make calls to object to get apporpriate data then write it
    extract = Extraction(dataFits)
    # extract.calculate_extraction(None)

    # get output from extract and write to file depending on arguments 

    # write images, figures, data, print info to user
    print('Extraction complete')

    newDir = os.path.join(baseDir, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(newDir)

    write_output_files(extract, newDir)
    write_figures(extract, newDir)

