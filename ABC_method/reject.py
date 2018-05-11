def reject(sim_sum_stats, emp_sum_stats, threshold, M, tau):
    """

    :param sim_sum_stats:
    :param emp_sum_stats:
    :param M:
    :param tau:
    :return:
    """
    # Average alpha
    emp_avg_alpha = []
    with open(emp_sum_stats, 'r') as f:
        for line in f:
            if not line.startswith('bins'):
                line = line.rstrip('\n')
                line = line.split('\t')
                emp_avg_alpha.append(float(line[2]))

    sim_avg_alpha=[]
    with open(sim_sum_stats, 'r') as f:
        for line in f:
            if not line.startswith('bins'):
                line = line.rstrip('\n')
                line = line.split('\t')
                sim_avg_alpha.append(float(line[3]))

    sum_avg_alpha = 0
    for i in range(0, len(emp_avg_alpha)):
        percentage = abs(emp_avg_alpha[i] - sim_avg_alpha[i])/emp_avg_alpha[i]
        sum_avg_alpha += percentage

    # # Number of SNPs
    # emp_num_SNPs = []
    # with open(emp_sum_stats, 'r') as f:
    #     for line in f:
    #         if not line.startswith('bins'):
    #             line = line.rstrip('\n')
    #             line = line.split('\t')
    #             emp_num_SNPs.append(float(line[1]))
    #
    # sim_num_SNPs=[]
    # with open(sim_sum_stats, 'r') as f:
    #     for line in f:
    #         if not line.startswith('bins'):
    #             line = line.rstrip('\n')
    #             line = line.split('\t')
    #             sim_num_SNPs.append(float(line[2]))
    #
    # sum_num_SNPs = 0
    # for i in range(0, len(emp_num_SNPs)):
    #     percentage = abs(emp_num_SNPs[i] - sim_num_SNPs[i])/emp_num_SNPs[i]
    #     sum_num_SNPs += percentage


    # if sum_avg_alpha <= threshold and sum_num_SNPs <= threshold:
    #     return (M, tau, sum)
    if sum_avg_alpha <= threshold:
        return (M, tau, sum_avg_alpha)
    else:
        return "Rejected"