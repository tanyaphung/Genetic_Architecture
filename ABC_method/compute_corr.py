import pandas as pd


def compute_corr(sel_maf_scaled_alpha_keep_outfile):

    data = pd.read_table(sel_maf_scaled_alpha_keep_outfile)
    data_keep = data[data.keep_or_discard == 'keep']
    pearson_corr = data_keep['maf'].corr(abs(data_keep['scaled_alpha']))

    return pearson_corr