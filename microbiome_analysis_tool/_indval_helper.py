import numpy as np

def _calculate_indval_score(asv_table, groups, asv, target_samples, unique_groups):
    """Helper function to calculate the IndVal score."""
    sum_mean_abundances = 0
    for g in unique_groups:
        sum_mean_abundances += asv_table.loc[groups.index[groups == g], asv].mean()

    if sum_mean_abundances == 0:
        return 0

    mean_abund_in_group = asv_table.loc[target_samples, asv].mean()
    specificity = mean_abund_in_group / sum_mean_abundances

    num_present_in_group = (asv_table.loc[target_samples, asv] > 0).sum()
    fidelity = num_present_in_group / len(target_samples)

    return np.sqrt(specificity * fidelity)
