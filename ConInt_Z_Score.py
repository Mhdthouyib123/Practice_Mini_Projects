# to import libraries
import numpy as np
import scipy.stats as st

# to get the confidence interval of the data

def con_intervel(data,confidence):
    z_score = st.norm.ppf(1-(1-confidence)/2) # to get the z score 
    mean_trans = data.mean()
    std_trans = np.std(data)
    length = len(data)
    moe = (z_score*std_trans)/np.sqrt(length) # to get the margin of error (second part of confidence interval formula after xbar)
    lower = float(round(mean_trans-moe,2)) # to get the lower value
    upper = float(round(mean_trans+moe,2)) # to get the higher value
    print(f'{int(confidence*100)}% confidence interval{lower,upper}')