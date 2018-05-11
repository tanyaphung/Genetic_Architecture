import argparse


def parse_args():
	"""
	Parse command-line arguments
	"""

	parser = argparse.ArgumentParser(description="Approximate Bayesian Computation to infer the coupling parameter"
												 "and the mutational target size for the Genetic Architecture project")

	inputs = parser.add_argument_group('inputs', 'Inputs.')

	outputs = parser.add_argument_group('outputs', 'Outputs.')

	inputs.add_argument("--directory", required=True,
						help="REQUIRED. Input a directory where the SLiM simulation outputs are stored.")

	inputs.add_argument("--emp", required=True,
						help="REQUIRED. Path to the empirical data. The file for empirical data should have 3 columns. "
							 "The first columns is the bins, the second column is the number of SNPs, and the "
							 "third column is the average alpha.")

	# inputs.add_argument("--tau", required=True,
	# 					help="REQUIRED. Input a value for tau.")
    #
	# inputs.add_argument("--M", required=True,
	# 					help="REQUIRED. Input a value for the mutational target size.")

	inputs.add_argument("--M_low", required=True,
						help="REQUIRED. Input a value for the low end for mutational target size.")

	inputs.add_argument("--M_high", required=True,
						help="REQUIRED. Input a value for the high end for mutational target size.")

	inputs.add_argument("--h2", required=True,
						help="REQUIRED. Input a value for the heritability.")

	inputs.add_argument("--N", required=True,
						help="REQUIRED. Input a value for the number of individuals in the GWAS."
							 "This parameter is used to compute power.")

	inputs.add_argument("--threshold", required=True,
						help="REQUIRED. Input a value for the threshold to reject.")

	# outputs.add_argument("--sel_maf", required=True,
	# 					help="REQUIRED. Path to the output file where the first column is the selection coefficient"
	# 						 "and the second column is the minor allele frequency. This file contains all of the SNPs"
	# 						 "for the mutational target size.")
    #
	# outputs.add_argument("--sel_maf_unscaled_alpha", required=True,
	# 					help="REQUIRED. Path to the output file where the first column is the selection coefficient, "
	# 						 "the second column is the minor allele frequency, and the third column is the unscaled "
	# 						 "alpha. This file contains all of the SNPs for the mutational target size.")
    #
	# outputs.add_argument("--sel_maf_scaled_alpha", required=True,
	# 					help="REQUIRED. Path to the output file where the first column is the selection coefficient, "
	# 						 "the second column is the minor allele frequency, the third column is the unscaled "
	# 						 "alpha, and the fourth column is the scaled alpha. This file contains all of the SNPs "
	# 						 "for the mutational target size.")
    #
	# outputs.add_argument("--sel_maf_scaled_alpha_keep", required=True,
	# 					help="REQUIRED. Path to the output file where:"
	# 						 "1. The first column is the selection coefficient, "
	# 						 "2. The second column is the minor allele frequency,"
	# 						 "3. The third column is the unscaled alpha, "
	# 						 "4. The fourth column is the scaled alpha, "
	# 						 "5. The fifth column is the power, and"
	# 						 "6. The sixth column tells you whether to keep or to discard this SNP based on power. "
	# 						 "This file contains all of the SNPs for the mutational target size.")

	# outputs.add_argument("--sum_stats", required=True,
	# 					help="REQUIRED. Path to the output file where the first column is the bins, the second"
	# 						 "column is the number of SNPs in that bin, and the third column is the average alpha.")
    #
	# outputs.add_argument("--accepted_vals", required=True,
	# 					help="REQUIRED. Path to the output file to store the values of M and tau that are accepted.")

	args = parser.parse_args()
	return args
