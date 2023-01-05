#!/bin/bash


# Name: genomes_downloader.sh
# Author: Ken Murithi
# Date: 5 Jan 2022

# The script downloads *Glossina* reference FASTA files from VectorBase database and indexes them

#create a txt file and store the six *Glossina* genome file paths
#nano genomes.txt

#create data directory to store the downloaded and indexed genome files 
mkdir -p data/{genomes,index_genomes} 

for genome in `cat genomes.txt`

do

base=$(basename $genome)

echo $base

wget $genome  -O ./data/genomes/${base}
bwa index ./data/genomes/${base} > ./data/index_genomes/${base}   # Index the respective reference genome

done
