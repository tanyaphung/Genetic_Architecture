from scipy.stats import norm
import numpy as np
import random


def npc(alpha, af, n):
    """
    This function computes the non-centrality parameter.
    :param alpha: allelic effect size
    :param af: allele frequency
    :param n: the number of individuals in a GWAS
    :return: npc
    """

    # Compute lambda
    # lambda_npc = alpha**2 * 2 * af * (1 - af)
    lambda_npc = abs(alpha) * (2 * af * (1 - af))**0.5 #modification after talking to Bogdan about how to compute power.

    # Compute npc
    npc = lambda_npc * n**0.5

    return npc

def power(npc, inv1, inv2):
    """
    This function computes power
    :param npc: This is the non-centrality parameter
    :return: power
    """
    power = norm.cdf(inv1 + npc) + 1 - norm.cdf(inv2 + npc)
    return power

def keep_or_discard(power):
    """
    This function keeps or discards a SNP based on power
    :param power: This is the power
    :return: "keep" or "discard"
    """

    # Generate a random number between 0 and 1
    rand_val = random.uniform(0, 1)
    if rand_val < power:
        string = 'keep'
        return string
    else:
        string = 'discard'
        return string

def select_snps(sel_maf_scaled_alpha_filename, n, outfile):
    """
    This function selects SNPs based on power. For each SNP, a random number between 0 and 1 is drawn.
    If the random number if less than power, than that SNP is kept. Otherwise, it is discarded.
    :param sel_maf_scaled_alpha_filename: This is the output from the script compute_scaled_alpha.py
    :param n: This is the number of people in the GWAS. For UKBioBank, it is around 500000
    :param outfile:
    :return: a file with 6 columns: (1) selection coefficient, (2) maf, (3) unscaled alpha, (4) scaled alpha, (5) power,
    and (6) keep or discard
    """

    # Pre-compute inv1 and inv2 to be passed as inputs to the power function.
    # Note that alpha used to compute p-value is hard-coded to be 5e-8 (after talking to Bogdan)
    alpha_p_val = 5e-8
    inv1 = norm.ppf(alpha_p_val/2, loc=0, scale=1)
    inv2 = norm.ppf(1-alpha_p_val/2, loc=0, scale=1)

    # Initialize the output file with header
    outfile = open(outfile, 'w')
    header = ['sel_coef', 'maf', 'unscaled_alpha', 'scaled_alpha', 'power', 'keep_or_discard']
    outfile.write('\t'.join(header) + '\n')

    # Initialize a list that stores all the npc for all of the SNPs. Convert this list later into a numpy array
    npc_snps = []

    # Initialize lists to be included in the output
    sel_coef=[]
    maf=[]
    unscaled_alpha=[]
    scaled_alpha=[]

    with open(sel_maf_scaled_alpha_filename, 'r') as f:
        for line in f:
            if not line.startswith('sel_coef'):
                line = line.rstrip('\n')
                line = line.split('\t')
                # Compute npc
                npc_snp = npc(float(line[3]), float(line[1]), n)
                npc_snps.append(npc_snp)

                sel_coef.append(line[0])
                maf.append(line[1])
                unscaled_alpha.append(line[2])
                scaled_alpha.append(line[3])

    # Convert the npc_snps list into an array
    npc_snps = np.asarray(npc_snps)

    # Compute power for all of the SNPs
    power_snps = power(npc_snps, inv1, inv2)

    for i in range(len(power_snps)):
        # Keep or discard
        to_print = [str(sel_coef[i]), str(maf[i]), str(unscaled_alpha[i]), str(scaled_alpha[i]), str(power_snps[i]), keep_or_discard(power_snps[i])]
        outfile.write('\t'.join(to_print) + '\n')

    outfile.close()
