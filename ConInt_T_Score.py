# to get the confidence interval of sample data (we have no idea about the population) using the t-score/t-test

import numpy as np
import scipy.stats as st

def t_test(data,confidence):
    count1=len(data)
    t_score = st.t.ppf(1-(1-confidence)/2,df=count1-1)
    data_mean = np.mean(data)
    std_data = np.std(data,ddof=1)
    moe = (t_score*std_data)/np.sqrt(count1)
    lower_point = float(round(data_mean-moe,2))
    upper_point = float(round(data_mean+moe,2))
    print(f'The {confidence*100}% confidence intervel of sales in Technolgy is {lower_point,upper_point}')
