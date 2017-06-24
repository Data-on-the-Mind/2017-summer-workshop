from numpy import *
from pylab import *
from pandas import read_pickle, merge, DataFrame

ANALYSIS_YEAR = 2012

resid_lott = read_pickle('data/log_resid_' + str(ANALYSIS_YEAR) + '_full.dat')

NUM_ZIPS = len(unique(resid_lott.ZIP))
IV =  'sum_pe_with_na'
DV = 'resid'

sports = read_pickle('data/sports_'+str(ANALYSIS_YEAR)+'.dat')

sports['date']= sports.index

for sports_col in ['sum_pe', 'sum_pe_with_na', 'mean_pe', 'p_win']: 
    sports[sports_col+'_lag_1'] = sports[sports_col].shift(1)
    

PE_BINS =  histogram(sports[~isnan(sports[IV])][IV],7)[1][1:].tolist() 
PE_BINS[1] -= .01 
PE_BIN_SIZE = PE_BINS[-1] - PE_BINS[-2]


for col in sports.columns:
    if(col not in ['p_win_lag_1', 'sum_streak_lag_1', 'sum_pe_lag_1', 'sum_pe_with_na_lag_1',
                   'percentile_sum_pe_lag_1', 'num_events', 'date']): 
        sports = sports.drop(col, 1)

resid_lott = merge(resid_lott, sports, on=['date']).set_index('date',drop=False)

[mean_sports_pe,sem_sports_pe] = [[],[]]
[mins, maxes] = [[],[]]


figure()
for bin_num in range(len(PE_BINS)):
    lower_pe = PE_BINS[bin_num] - PE_BIN_SIZE
    upper_pe = PE_BINS[bin_num]

    bin_dv = resid_lott[logical_and(resid_lott[IV+'_lag_1']>lower_pe,
                                    resid_lott[IV+'_lag_1']<=upper_pe)].groupby('ZIP').aggregate(mean)[DV]

    mean_sports_pe.append( mean(bin_dv) ) 
    n = NUM_ZIPS 
    sem_sports_pe.append( std(bin_dv) / sqrt(len(bin_dv))) #sqrt(n)) 



errorbar(PE_BINS[:], mean_sports_pe[:],yerr=sem_sports_pe[:], color='blue', lw = 1.5, ecolor='black',
         capsize=5, label='NYC Teams', marker='o')

plot([PE_BINS[0]-1,PE_BINS[-1]+.5], [0,0], color='gray', ls=':')
xlabel('Sum PE')
ylabel('Residual Composite Per Capita Purchases') #(DV+' ')
show()

