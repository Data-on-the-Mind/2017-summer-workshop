import gzip, os
from numpy import *
from pylab import *
from scipy.stats import zscore, pearsonr, linregress, scoreatpercentile
from pandas import DataFrame, date_range, Series, datetools, tseries, rolling_mean, rolling_std, ols, concat, HDFStore, merge, read_csv, read_pickle, to_numeric
import urllib2, csv, re, cPickle, calendar, time
from datetime import datetime
import statsmodels.api as sm
import statsmodels.formula.api as smf

DATE_RANGES = {2011:  date_range(datetime(2011, 1, 1), datetime(2011, 12,31)),
               2012: date_range(datetime(2012, 1, 1), datetime(2012, 12,31))}
ANALYSIS_YEAR = 2012
analysis_range = DATE_RANGES[ANALYSIS_YEAR]

lott = read_pickle('data/'+str(ANALYSIS_YEAR)+'_lottery_sales.dat')
lott['date'] = lott.index

lott['composite'] = (lott['Take5'] + lott['Win4Day'] + lott['Win4Eve'] +lott['QuickDraw'] +   lott['Pick10'] +lott['NumbersDay'] + lott['NumbersEve'] ) 


demographics = read_pickle('data/demographics.dat')
zoning = read_pickle('data/zoning.dat')

demographics = merge(demographics, zoning, on='ZIP')
demographics.index = demographics.ZIP.astype(int)


low_residential_zips = demographics[demographics.prop_residential < .4].index
for exclude_zip in low_residential_zips:
    lott = lott[(lott.ZIP != exclude_zip)]
    print 'excluding:', exclude_zip, demographics.ix[exclude_zip].desc
    
    
print 'excluded ', len(low_residential_zips), 'low residential density ZIPs'

lott['composite_per_capita'] = zeros(lott.shape[0])
grouped = lott.groupby('ZIP')
for zip, zip_lott in grouped:
    lott.ix[lott.ZIP==zip,'composite_per_capita'] = lott[lott.ZIP==zip]['composite'] / demographics.ix[zip]['population_over_18']


