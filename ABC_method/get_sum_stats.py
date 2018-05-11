import pandas as pd
import numpy as np


def get_num_SNPs_prior(sel_maf_scaled_alpha_filename):
    """
    This function obtains the number of SNPs in each bin using the data PRIOR to filtering based on power for each replicate.
    This is to calculate the fraction of the SNPs in each bin that are remained after filtering based on power.
    :param sel_maf_scaled_alpha_filename:
    :return: 1 dictionary
    """
    data = pd.read_table(sel_maf_scaled_alpha_filename)

    # Bin the data by maf. Right now the binning is hard-coded, but this could be made into a parameter.
    # Bin 1 (0-0.5%).
    # Bin 2 (0.5-1%).
    # Bin 3 (1-5%).
    # Bin 4 (5-10%).
    # Bin 5: (10-20%).
    # Bin 6: (20-50%).
    bin1 = data[(data.maf <= 0.005)]
    bin2 = data[(data.maf > 0.005) & (data.maf <= 0.01)]
    bin3 = data[(data.maf > 0.01) & (data.maf <= 0.05)]
    bin4 = data[(data.maf > 0.05) & (data.maf <= 0.1)]
    bin5 = data[(data.maf > 0.1) & (data.maf <= 0.2)]
    bin6 = data[(data.maf > 0.2)]

    num_SNPs = {}
    num_SNPs['1:0-0.5%'] = len(bin1)
    num_SNPs['2:0.5-1%'] = len(bin2)
    num_SNPs['3:1-5%'] = len(bin3)
    num_SNPs['4:5-10%'] = len(bin4)
    num_SNPs['5:10-20%'] = len(bin5)
    num_SNPs['6:20-50%'] = len(bin6)

    return num_SNPs

def get_num_SNPs_avg_alpha_post(sel_maf_scaled_alpha_keep_filename):
    """
    This function obtains the number of SNPs in each bin using the data POST filtering based on power for each replicate.
    :param sel_maf_scaled_alpha_keep_filename:
    :return: 3 dictionaries
    """
    data = pd.read_table(sel_maf_scaled_alpha_keep_filename)

    # Subset the data to include the "keep SNPs"
    data_keep = data[data.keep_or_discard == 'keep']

    # Bin the data by maf. Right now the binning is hard-coded, but this could be made into a parameter.
    # Bin 1 (0-0.5%).
    # Bin 2 (0.5-1%).
    # Bin 3 (1-5%).
    # Bin 4 (5-10%).
    # Bin 5: (10-20%).
    # Bin 6: (20-50%).
    bin1 = data_keep[(data_keep.maf <= 0.005)]
    bin2 = data_keep[(data_keep.maf > 0.005) & (data_keep.maf <= 0.01)]
    bin3 = data_keep[(data_keep.maf > 0.01) & (data_keep.maf <= 0.05)]
    bin4 = data_keep[(data_keep.maf > 0.05) & (data_keep.maf <= 0.1)]
    bin5 = data_keep[(data_keep.maf > 0.1) & (data_keep.maf <= 0.2)]
    bin6 = data_keep[(data_keep.maf > 0.2)]

    # Number of SNPs post filtering for power
    num_SNPs_post = {}
    num_SNPs_post['1:0-0.5%'] = len(bin1)
    num_SNPs_post['2:0.5-1%'] = len(bin2)
    num_SNPs_post['3:1-5%'] = len(bin3)
    num_SNPs_post['4:5-10%'] = len(bin4)
    num_SNPs_post['5:10-20%'] = len(bin5)
    num_SNPs_post['6:20-50%'] = len(bin6)

    # Average effect size
    avg_alpha_post = {}

    if len(bin1) != 0:
        avg_alpha_post['1:0-0.5%'] = np.mean(abs(bin1.scaled_alpha))
    else:
        avg_alpha_post['1:0-0.5%'] = 0

    if len(bin2) != 0:
        avg_alpha_post['2:0.5-1%'] = np.mean(abs(bin2.scaled_alpha))
    else:
        avg_alpha_post['2:0.5-1%'] = 0

    if len(bin3) != 0:
        avg_alpha_post['3:1-5%'] = np.mean(abs(bin3.scaled_alpha))
    else:
        avg_alpha_post['3:1-5%'] = 0

    if len(bin4) != 0:
        avg_alpha_post['4:5-10%'] = np.mean(abs(bin4.scaled_alpha))
    else:
        avg_alpha_post['4:5-10%'] = 0

    if len(bin5) != 0:
        avg_alpha_post['5:10-20%'] = np.mean(abs(bin5.scaled_alpha))
    else:
        avg_alpha_post['5:10-20%'] = 0

    if len(bin6) != 0:
        avg_alpha_post['6:20-50%'] = np.mean(abs(bin6.scaled_alpha))
    else:
        avg_alpha_post['6:20-50%'] = 0

    # return num_SNPs_post, avg_alpha_post
    return num_SNPs_post, avg_alpha_post

