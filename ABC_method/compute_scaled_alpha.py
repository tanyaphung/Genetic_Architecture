def compute_scaled_alpha(h2, sel_maf_unscaled_alpha_filename, outfile):
    """
    This script computes (scaled) alpha by first computing the normalizing constant c (see Lohmueller 2014 PLoS Genetics
    method section for more details)
    :param h2: heretability estimate
    :param sel_maf_unscaled_alpha_filename: output from the script compute_unscaled_alpha.py
    :param outfile:
    :return: a file with 4 columns: selection coefficient, maf, unscaled alpha, and scaled alpha
    """

    outfile = open(outfile, 'w')
    header = ['sel_coef', 'maf', 'unscaled_alpha', 'scaled_alpha']
    outfile.write('\t'.join(header) + '\n')

    total_var = []
    with open(sel_maf_unscaled_alpha_filename, 'r') as f:
        for line in f:
            if not line.startswith('sel_coef'):
                line = line.rstrip('\n')
                line = line.split('\t')
                var = 2 * float(line[1]) * (1 - float(line[1])) * float(line[2])**2
                total_var.append(var)

    # Compute the scaling factor c
    c = (h2/sum(total_var))**0.5

    # Compute scaled_alpha by multiplying unscaled_alpha by the scaling factor c
    with open(sel_maf_unscaled_alpha_filename, 'r') as f:
        for line in f:
            if not line.startswith('sel_coef'):
                line = line.rstrip('\n')
                line = line.split('\t')
                scaled_alpha = float(line[2]) * c
                to_print = [line[0], line[1], line[2], str(scaled_alpha)]
                outfile.write('\t'.join(to_print) + '\n')

    outfile.close()
