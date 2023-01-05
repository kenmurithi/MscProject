#! /bin/bash

# Name: CisBP2MEME.sh
# Author: Ken Murithi
# Date: 5 Jan 2023

# The script convert Cis-BP motif matrixes to  meme format

import os, glob
import pandas as pd
import numpy as np


import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument(
    "--dir",
    type=str,
    dest="dir",
    action="store",
    help="path to pwm motif files",
    default="pwms_all_motifs",
)
parser.add_argument(
    "--tf_info",
    type=str,
    dest="tf_info",
    action="store",
    help="TF information file",
    default="TF_Information_all_motifs_plus.txt",
)
parser.add_argument(
    "--output",
    type=str,
    dest="output",
    action="store",
    help="Output motif file in meme format",
    default="CiSBP_latest.meme",
)

parser.add_argument(
    "--species",
    type=str,
    dest="species",
    action="store",
    help="Set species of the motifs",
    default="Unknown_species",
)



args = parser.parse_args()


files = glob.glob('{}/*'.format(args.dir))
pwms = [x.split('/')[1].split('.txt')[0] for x in files]

url_prefix = 'http://cisbp.ccbr.utoronto.ca/TFreport.php?searchTF='

mapping = pd.read_csv(args.tf_info, header=0, sep='\t')
mapping = mapping[['Motif_ID', 'TF_ID', 'TF_Name', 'TF_Status']]
mapping.sort_values(['Motif_ID', 'TF_Status'])
mapping = mapping[mapping['Motif_ID'] != '.']
newmapping = mapping.groupby(['Motif_ID']).apply(lambda x: x.iloc[0])
newmapping.set_index('Motif_ID', inplace=True)

with open(args.species+'_'+args.output, 'w') as f:
    f.writelines('MEME version 4\n')
    f.writelines('\n')
    f.writelines('ALPHABET= ACGT\n')
    f.writelines('\n')
    f.writelines('strands: + -\n')
    f.writelines('\n')
    f.writelines('Background letter frequencies (from uniform background):\n')
    f.writelines('A 0.25000 C 0.25000 G 0.25000 T 0.25000 \n')
    f.writelines('\n')

    for idx, pwm in enumerate(pwms[:]):
        print(idx,pwm)
        with open(os.path.join(args.dir,pwm+'.txt'), 'r') as s:
            data = s.readlines()
            l = len(data) - 1

        f.writelines('MOTIF {} {}\n'.format(pwm, newmapping.loc[pwm]['TF_Name']))
        f.writelines('\n')
        f.writelines('letter-probability matrix: alength= 4 w= {} nsites= 1 E= 0\n'.format(l))
        for i in range(1, len(data)):
            numbers = data[i].rstrip().split('\t')
            _sum = np.sum([float(numbers[1]), float(numbers[2]), float(numbers[3]), float(numbers[4])])
            f.writelines('  {}    {}      {}      {}    \n'.format(float(numbers[1]) / _sum, float(numbers[2]) / _sum,
                                                                     float(numbers[3]) / _sum,
                                                                     float(numbers[4]) / _sum))
        f.writelines('\n')
        f.writelines('URL {}\n'.format(url_prefix + newmapping.loc[pwm]['TF_ID']))
        f.writelines('\n')
