def process_slim_outputs(filenames, outfile):
    """
    This function processes the SLiM output by obtaining the minor allele frequency and the selection coefficient
    for each SNP.
    :param filenames:
    :param outfile:
    :return:
    """
    outfile = open(outfile, 'w')
    header = ['sel_coef', 'maf']
    outfile.write('\t'.join(header) + '\n')
    for filename in filenames:
        n_genomes = 0
        with open(filename, 'r') as f:
            for line in f:
                if line.startswith('#'):
                    line = line.rstrip("\n")
                    line = line.split(" ")
                    n_genomes = float(line[4])
                else:
                    if not line.startswith('Mutations') and not line.startswith('Genomes') and not \
                            line.startswith('p1'):
                        line = line.rstrip("\n")
                        line = line.split(" ")
                        af = (float(line[8]))/n_genomes
                        if af <= 0.5:
                            to_print = [line[4], str(af)]
                            outfile.write('\t'.join(to_print) + '\n')
                        else:
                            maf = 1 - af
                            to_print = [line[4], str(maf)]
                            outfile.write('\t'.join(to_print) + '\n')
    outfile.close()
