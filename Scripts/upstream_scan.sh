#!/bin/bash

# Name: upstream_scan.sh
# Author: Ken Murithi
# Date: 5 Jan 2022

# Motif-collection contains the motifs
# Copy the Motif-collection path, eg of the Acj6.meme file
# cd to one of the Glossina directory storing the Ors upstream.fa

for upstream in *

do

base=$(basename ${upstream})
base2=$(basename $base .meme)

echo 'running' $base2

fimo $upstream  ./Motif-collection/Acj6.meme -o ${upstream}__binding_sites # An example of using Acj6 motif to scan through Glossina austeni upstream fasta files

done
