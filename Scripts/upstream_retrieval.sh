#!/bin/bash


# Name: upstream_retrieval.sh
# Author: Ken Murithi
# Date: 5 Jan 2022

#create a directory with bed files for each of the Glossina species
#For example: nano Gau-or # this directory contins bed files for the glossina austeni chemosensory genes

for bed in  *.bed

do

base=$(basename ${bed})
base2=$(basename $base .bed)

echo 'running' $base2

bedtools flank -i $bed -g Gau.genome -l 500 -r 0 >  ${base2}_upstream.bed # extracts the upstream (500bp) region of the chemosensory genes
bedtools getfasta -fi ./data/index_genomes/${genome} -bed ${base2}_upstream.bed >${base2}_upstream.fa #gets the fasta file of the extracted upstream region

done
