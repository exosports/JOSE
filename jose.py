#!/usr/bin/env python3

import numpy as np
import logging
import yaml
import datetime
import sys
import argparse
import os
from astropy.io import fits as pyfits

from jose.Extraction import Extraction

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

def create_template(directory, filename):
    r'''Creates template YAML config file in specified directory'''
    raise NotImplementedError()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract spectral data from FITS image")
    parser.add_argument('-o' , "--output-dir",
        help="Directory to output results, defaults to current working directory")
    configFileGroup = parser.add_mutually_exclusive_group(required=True)
    configFileGroup.add_argument('-c', "--config",
        help="Configuration file with extraction options")
    configFileGroup.add_argument('-r', "--regenerate-config",
        help="Creates a template config file with the specified name")
    args = parser.parse_args()

    #TODO: create process args function to clean up main
    if args.output_dir == None: # default to cwd
        output_dir = os.getcwd();
    else:
        output_dir = args.output_dir

    if not args.regenerate_config == None: # create standard template file
        create_template(output_dir, args.regenerate_config)
        sys.exit()

    # read in config file
    with open(args.config, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    print(cfg)
    # object bounds need to be supplied by the user
    # require output directory
    data    = pyfits.open(cfg['data'])[0] 
    baseDir = os.path.join(os.getcwd(), cfg['outdir']) 

    extract = Extraction(data)
    extract.calculate_extraction(options = cfg) 

    # get output from extract and write to file depending on arguments 

    # write images, figures, data, print info to user
    print('Extraction complete.')

    newDir = os.path.join(baseDir,
                          datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(newDir)

    write_output_files(extract, newDir)
    write_figures(extract, newDir)

