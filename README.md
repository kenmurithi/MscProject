
# Ken's_MSc_Project
## Project Overview
### Project tittle
Comparative modelling of Transcription Factors Binding Sites Regulating Chemosensory Gene Family Expression in Six *Glossina* Species
### Background
Tsetse flies (genus *Glossina*) are the sole vectors of human and animal trypanosomiasis in 38 sub-Saharan African countries. Despite the success of the tsetse capture, the divergence in responding to the available odour traps has been observed in various tsetse species,thus preventing the development of a global vector control method. The differences in TF binding specificities on chemosensory genes could explain the divergence in the gene expression levels. Thus, this study focused on examining the differential binding site specificities of the TFs regulating the chemosensory genes
### Objectives
1.	To identify all transcription factors in the six *Glossina* species using *Drosophila melanogaster* homologs. 
2.	To model chemosensory transcription factors binding specificities in *Glossina* using models (PWMs) from *Drosophila melanogaster*. 
3.	To predict and compare binding sites in the six *Glossina* species using the modelled PWMs.
### Pipeline
The tools used for this project include:

* `BWA` for indexing the *Glossina* reference genomes
* `bedtools flank` for creating flanking intervals for each BED file
* `bedtools getfasta` for extracting sequences from a FASTA file for each of the intervals defined in a BED file
* `fimo` for searching motifs from the upstream FASTA files
* `meme2images` for generating logo images from MEME files

The pipeline used in this project:

![image](https://user-images.githubusercontent.com/59683723/210792999-f5b65ac9-c416-4329-bf3a-8435a9d9aa0d.png)

