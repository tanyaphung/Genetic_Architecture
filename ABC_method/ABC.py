from parse_args import *
from get_slim_outputs import *
from process_slim_outputs import *
from compute_unscaled_alpha import *
from compute_scaled_alpha import *
from select_SNPs_based_on_power import *
from get_sum_stats import *
from reject import *
import shutil
import numpy
import os
from numpy import random
# from compute_corr import *

def main():

    args = parse_args()

    # Step 0: randomly generating a value for tau and M from a uniform distribution.
    tau = numpy.random.uniform(low=0.0, high=1.0, size=None)
    m = int(numpy.random.uniform(low=args.M_low, high=args.M_high, size=None)/100000)*100000

    # Make the directory
    os.makedirs('tau_' + str(tau) + '_M_' + str(m))

    # Step 1: get slim outputs, which depends on the value of M
    # filenames = get_slim_outputs(directory=args.directory, m=float(args.M))
    filenames = get_slim_outputs(directory=args.directory, m=m)

    # Process slim output to obtain selection and minor allele frequency
    # process_slim_outputs(filenames=filenames, outfile=args.sel_maf)
    process_slim_outputs(filenames=filenames, outfile='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf.out')

    # Compute (unscaled) alpha
    # compute_unscaled_alpha(tau=float(args.tau), sel_maf_filename=args.sel_maf, outfile=args.sel_maf_unscaled_alpha)
    # compute_unscaled_alpha(tau=tau, sel_maf_filename=args.sel_maf, outfile=args.sel_maf_unscaled_alpha)
    compute_unscaled_alpha(tau=tau, sel_maf_filename='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf.out', outfile='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_unscaled_alpha.out')

    # Compute (scaled) alpha
    # compute_scaled_alpha(h2=float(args.h2), sel_maf_unscaled_alpha_filename=args.sel_maf_unscaled_alpha,
    #                      outfile=args.sel_maf_scaled_alpha)
    compute_scaled_alpha(h2=float(args.h2), sel_maf_unscaled_alpha_filename='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_unscaled_alpha.out', outfile='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_scaled_alpha.out')

    # Obtain the number of SNPs in each maf bin using the data prior to filtering based on power
    num_SNPs_prior = get_num_SNPs_prior('tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_scaled_alpha.out')

    # Select SNPs based on power
    # select_snps(sel_maf_scaled_alpha_filename=args.sel_maf_scaled_alpha, n=float(args.N), outfile=args.sel_maf_scaled_alpha_keep)
    select_snps(sel_maf_scaled_alpha_filename='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_scaled_alpha.out', n=float(args.N), outfile='tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_scaled_alpha_keep.out')

    # results (below) is a tuple where the first item is the num_SNPs, the second item is the avg_alpha
    results = get_num_SNPs_avg_alpha_post('tau_' + str(tau) + '_M_' + str(m) + '/sel_maf_scaled_alpha_keep.out')

    num_SNPs_post = results[0]
    avg_alpha_post = results[1]

    # Open the sum_stats_outfile and initialize with header
    # sum_stats_outfile = open(args.sum_stats, 'w')
    sum_stats_outfile = open('tau_' + str(tau) + '_M_' + str(m) + '/sum_stats.out', 'w')
    header = ["bins", "num_SNPs_prior", "num_SNPs_post", "avg_abs_scaled_alpha_post"]
    sum_stats_outfile.write('\t'.join(header) + '\n')

    for k in sorted(num_SNPs_prior):
        to_print = [k, str(num_SNPs_prior[k]), str(num_SNPs_post[k]), str(avg_alpha_post[k])]
        sum_stats_outfile.write('\t'.join(to_print) + '\n')
    sum_stats_outfile.close()

    # Reject the (M, tau) parameter or not
    # reject_results = reject(args.sum_stats, args.emp, float(args.threshold), args.M, args.tau)
    reject_results = reject('tau_' + str(tau) + '_M_' + str(m) + '/sum_stats.out', args.emp, float(args.threshold), m, tau)
    if reject_results is not 'Rejected':
        # accepted_vals_outfile = open(args.accepted_vals, 'a')
        accepted_vals_outfile = open('tau_' + str(tau) + '_M_' + str(m) + '/accepted_vals.out', 'a')
        to_print = [str(reject_results[0]), str(reject_results[1]), str(reject_results[2])]
        accepted_vals_outfile.write('\t'.join(to_print) + '\n')
        accepted_vals_outfile.close()
    else:
        # shutil.rmtree('/u/home/p/phung428/nobackup-kirk/tanya_data/Gen_Architecture_Project/outputs/ABC_height_050418_grid/tau_' + args.tau + '_M_' + args.M)
        shutil.rmtree(
            'tau_' + str(tau) + '_M_' + str(m))

if __name__ == '__main__':
    main()
