# to calculate t statistics and answer the above question / problem

import numpy as np
import scipy.stats as st

def t_stats_hypo(data,hypo_mean):
    n=len(data)
    dof = n-1
    mean_data = np.mean(data)
    std_data = np.std(data)
    t_statistics = (mean_data-hypo_mean) / (std_data/np.sqrt(n)) # calculate the T statistics
    p_value  = 2*(1-st.t.cdf(abs(t_statistics),dof)) # calculate p value for two tailed test
    print('T-Statistics : ',round(t_statistics,4))
    print('P-Value : ',round(p_value,4))

    alpha = 0.05
    if p_value < alpha:
        print('Reject H0 : The average profit for Furniture is not $300.')
    else:
        print('Failed to Reject H0 : The average profit for Furniture is $300.')