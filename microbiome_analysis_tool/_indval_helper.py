import numpy as np

def _calculate_indval_score(asv_table, asv, target_samples, sum_mean_abundances):
    """Helper function to calculate the IndVal score."""
    if sum_mean_abundances == 0:
        return 0

    mean_abund_in_group = asv_table.loc[target_samples, asv].mean()
    specificity = mean_abund_in_group / sum_mean_abundances

    num_present_in_group = (asv_table.loc[target_samples, asv] > 0).sum()
    fidelity = num_present_in_group / len(target_samples)

    return np.sqrt(specificity * fidelity)
