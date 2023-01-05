
#!/bin/bash

# Script Name: gff_downloader.sh
# Author: Ken Murithi
# Date: 5 Jan 2022

# Description: Download gff files from a text file containing gff file paths. A genome file is also created.
# Automatically downloads the fastq files in the Data/gffs dir in your working dir

# Create a txt file to  the gff file paths
# nano gff.txt

for gff in `cat gff.txt`

do

base=$(basename ${gff})
base2=$(basename $base .gff)

wget $gff  -O ./data/gffs/${base}
grep "protein_coding_gene" ./data/gffs/${base} | cut -f 1,4,5 > ./data/genome_files/${base2}genome  #creating a genome file

done
