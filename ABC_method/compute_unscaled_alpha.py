import numpy as np
import random


def compute_unscaled_alpha(tau, sel_maf_filename, outfile):
    """
    This script computes (unscaled) alpha by using Eyre-Walker's model. See the method section in Lohmueller 2014
    PLoS Genetics for more details
    :param tau:
    :param sel_maf_filename: this is the output file from the script process_slim_outputs.py
    :param outfile:
    :return: a file with 3 columns: selection coefficient, maf, and unscaled alpha
    """
    outfile = open(outfile, 'w')
    header = ['sel_coef', 'maf', 'unscaled_alpha']
    outfile.write('\t'.join(header) + '\n')

    with open(sel_maf_filename, 'r') as f:
        for line in f:
            if not line.startswith('sel_coef'):
                line = line.rstrip('\n')
                line = line.split('\t')
                delta = random.choice([-1, 1])
                sel = float(line[0])
                epsilon = np.random.normal(0, 0.5, 1)[0]
                alpha = delta * abs(sel)**tau * (1+epsilon)
                to_print = [line[0], line[1], str(alpha)]
                outfile.write('\t'.join(to_print) + '\n')
    outfile.close()
