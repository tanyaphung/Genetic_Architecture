# Inferring the genetic architecture and extent of negative selection of human complex traits

This repository contains scripts associated with the manuscript titled "Inferring the genetic architecture and extent of negative selection of human complex traits" (in prep)

## ABC_method
* This directory contains scripts used to infer tau and M
* Usage:
```
python ABC.py -h                                                  
usage: ABC.py [-h] --directory DIRECTORY --emp EMP --M_low M_LOW --M_high
              M_HIGH --h2 H2 --N N --threshold THRESHOLD

Approximate Bayesian Computation to infer the coupling parameterand the
mutational target size for the Genetic Architecture project

optional arguments:
  -h, --help            show this help message and exit

inputs:
  Inputs.

  --directory DIRECTORY
                        REQUIRED. Input a directory where the SLiM simulation
                        outputs are stored.
  --emp EMP             REQUIRED. Path to the empirical data. The file for
                        empirical data should have 3 columns. The first
                        columns is the bins, the second column is the number
                        of SNPs, and the third column is the average alpha.
  --M_low M_LOW         REQUIRED. Input a value for the low end for mutational
                        target size.
  --M_high M_HIGH       REQUIRED. Input a value for the high end for
                        mutational target size.
  --h2 H2               REQUIRED. Input a value for the heritability.
  --N N                 REQUIRED. Input a value for the number of individuals
                        in the GWAS.This parameter is used to compute power.
  --threshold THRESHOLD
                        REQUIRED. Input a value for the threshold to reject.

outputs:
  Outputs.

```
