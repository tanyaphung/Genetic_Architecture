from scipy.stats import poisson
import random
import argparse

def parse_args():
    """
    Parse command-line arguments
    :return:
    """

    parser = argparse.ArgumentParser(description="This script selects (tau, M) pairs based on the number of SNPs, by computing sum of squared difference")

    parser.add_argument("--emp_data", required=TRUE,
                        help="REQUIRED. Path to the empirical data.")

    parser.add_argument("--accepted_vals", required=TRUE,
                        help="REQUIRED. Path to the accepted vals file.")

    parser.add_argument("--directory", required=TRUE,
                        help="REQUIRED.")

    parser.add_argument("--outfile", required=TRUE,
                        help="REQUIRED. Path to the output file.")

    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    outfile = open(args.outfile, 'w')

    emp = []
    with open(args.emp_data, 'r') as f:
        for line in f:
            if not line.startswith("bins"):
                line = line.rstrip('\n')
                line = line.split('\t')
                emp.append(int(line[1]))

    with open(args.accepted_vals, 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            line = line.split('\t')
            m = line[0]
            tau = line[1]

            # Get the sum_stats.out for the (m, tau) pair
            sim = []
            with open(args.directory + '/tau_'+ tau + '_M_' + m + '/sum_stats.out', 'r') as f:
                for line in f:
                    if not line.startswith('bins'):
                        line = line.rstrip('\n')
                        line = line.split('\t')
                        sim.append(int(line[2]))

            # Compute sum of squared difference
            sum_sq_diff = 0
            for i in range(len(emp)):
                sq_diff = (sim[i] - emp[i]) ** 2
                sum_sq_diff += sq_diff

            to_print = [m, tau, str(sum_sq_diff)]
            outfile.write('\t'.join(to_print) + '\n')

main()


# outfile = open('/u/home/p/phung428/height_sum_squared.out', 'w')
#
# with open('/u/home/p/phung428/accepted_vals.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip('\n')
#         line = line.split('\t')
#         m = line[0]
#         tau = line[1]
#
#         # Get the sum_stats.out for the (m, tau) pair
#         sim=[]
#         with open('/u/flashscratch/p/phung428/tmp/050818_temp/tau_' + tau + '_M_' + m + '/sum_stats', 'r') as f:
#             for line in f:
#                 if not line.startswith('bins'):
#                     line = line.rstrip('\n')
#                     line = line.split('\t')
#                     sim.append(int(line[2]))
#         # print (sim)
#
#         # probs = 1
#         #
#         # for i in range(len(emp)):
#         #     prob = poisson.pmf(emp[i], sim[i])/poisson.pmf(emp[i], emp[i])
#         #     probs = probs * prob
#         #
#         # # Pick a random number
#         #
#         # rand_n = random.uniform(0,1)
#         #
#         # if rand_n <= probs:
#         #     text = 'keep'
#         #     to_print = [m, tau, str(probs), str(rand_n), text]
#         #     outfile.write('\t'.join(to_print) + '\n')
#         # else:
#         #     text='discard'
#         #     to_print = [m, tau, str(probs), str(rand_n), text]
#         #     outfile.write('\t'.join(to_print) + '\n')
#
#         # Compute sum of squared difference
#         sum_sq_diff = 0
#         for i in range(len(emp)):
#             sq_diff = (sim[i] - emp[i])**2
#             sum_sq_diff += sq_diff
#
#         to_print = [m, tau, str(sum_sq_diff)]
#         outfile.write('\t'.join(to_print) + '\n')