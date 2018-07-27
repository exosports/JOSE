import numpy as np
import logging
import configargparse
import yaml
import datetime
import os
from astropy.io import fits as pyfits

from Extraction import Extraction

log = logging.getLogger(__name__)

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
    f, ax = extraction.make_spectrum_figure()
    f.savefig(os.path.join(targetDir, 'spectrum.png'))
    # TODO: output image, fitted profile, other useful stuff, inspired by IDL plottype flags from other code


if __name__ == "__main__":
    print(os.getcwd())
    p = configargparse.ArgParser(default_config_files=[r'./jose/config.yaml'], config_file_parser_class=configargparse.YAMLConfigFileParser )
    p.add('-c', '--config', required=True, is_config_file=True, help='config file path')
    p.add('--degree', required=False, help='path to genome file')

    options = p.parse_args()

    print(options)

    with open(options['config'], 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    print(cfg)

    # object bounds need to be supplied by the user
    # require output directory
    dataFits = pyfits.open(os.path.join('images', 'ex1.fits'))[0] #TODO: get from argparser
    baseDir = os.path.join(os.getcwd(), 'outputTests') #TODO: parse from command line

    # this should deal with all file I/O, make calls to object to get apporpriate data then write it
    extract = Extraction(dataFits)
    extract.calculate_extraction(
        options = {'object_bounds' : (240, 270) }) #TODO: inelegant, maybe make static method to create object or function call

    # get output from extract and write to file depending on arguments 

    # write images, figures, data, print info to user
    print('Extraction complete')

    newDir = os.path.join(baseDir, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(newDir)

    write_output_files(extract, newDir)
    write_figures(extract, newDir)

