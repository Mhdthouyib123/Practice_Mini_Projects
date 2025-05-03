# to create a new function to get the statistics our own

def calc_fo(data):
        import numpy as np
        import pandas as pd
        import scipy.stats as st

        total_sum=sum(data)
        print('Total Revenue',total_sum)

        count=len(data)
        print('Total Count',count)

        avg=total_sum/count
        print('Mean',avg)

        med=np.median(data)
        print('Median',med)

        mode_val,mode_count=st.mode(data)
        print('Mode',mode_val)

        low=min(data)
        print('Minimum',low)

        high=max(data)
        print('Maximum',high)

        ran=high-low
        print('Range',ran)

        vary=np.var(data)
        print('Variance',vary)

        sd=np.std(data)
        print('Standard Deviation',sd)

        q1= np.percentile(data,25)
        print('Quartile 1',q1)

        q3= np.percentile(data,75)
        print('Quartile 3',q3)

        iqr= q3-q1
        print('Inter Quartile Range',iqr)

        lw=q1-(iqr*1.5)
        print('Lower Whisker',lw)

        uw=q3+(iqr*1.5)
        print('Upper Whisker',uw)

        sk = st.skew(data)
        print(sk)

        ku = st.kurtosis(data)
        print(ku)
    