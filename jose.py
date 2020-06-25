#!/usr/bin/env python3

import numpy as np
import logging
import yaml
import datetime
import sys
import argparse
import os
import astropy.io.fits as fits

import jose

log = logging.getLogger(__name__)

# TODO: should this copy the data?
def write_output_files(extraction, resdir):
    r'''Writes results of extraction to resdir

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
    np.savetxt(os.path.join(resdir, 'spec.txt'), extraction.optimal_spectrum)

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
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # object bounds need to be supplied by the user
    # require output directory
    hdulist   = fits.open(cfg['data']) 
    outputdir = os.path.join(os.getcwd(), cfg['outdir'])

    if not os.path.isdir(outputdir):
        os.makedirs('output')

    try:
        fnum = cfg['fnum']
    except KeyError:
        fnum = 0

    extract = jose.extraction.Extraction(hdulist[fnum], cfg)
    extract.calculate_extraction() 

    # get output from extract and write to file depending on arguments 

    # write images, figures, data, print info to user
    print('Extraction complete.')
        
    resdir = os.path.join(outputdir,
                          datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+
                          '-' + cfg['label'])
    os.makedirs(resdir)

    write_output_files(extract, resdir)
    write_figures(extract, resdir)
    extract.save(os.path.join(resdir, 'extract.obj'))

