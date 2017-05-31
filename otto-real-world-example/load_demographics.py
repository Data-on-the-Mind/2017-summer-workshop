from pandas import DataFrame, concat, read_pickle, Series
from pandas.io.excel import read_excel
from HTMLParser import HTMLParser
from numpy import isnan, isreal, repeat, shape
from scipy.stats import zscore
import sys, cPickle,os
import random, urllib2

def extractListFromURL(data_source, variable, year):
    if(data_source=='sf1'):
        url = 'http://api.census.gov/data/2010/sf1?key=2ce6c596b79f689bd990b6213d1ed4aacbba3f75&get=' + variable + '&in=state:36&for=zip+code+tabulation+area'
    elif(data_source=='acs5'):
        url = 'http://api.census.gov/data/'+str(year)+ '/acs5?key=2ce6c596b79f689bd990b6213d1ed4aacbba3f75&get=' + variable + '&for=zip+code+tabulation+area:*'

    response = urllib2.urlopen(url)
    resp_text = response.read().split('\n') 
    if(data_source=='sf1'):
        data = map(lambda x:map(int, x.replace(']', '').replace('[', '').replace('"','').split(',')[0:3]), resp_text[1:])
    elif(data_source=='acs5'):
        resp_text = filter(lambda x: 'null' not in x, resp_text)
        data = map(lambda x:map(int, x.replace(']', '').replace('[', '').replace('"','').split(',')[0:2]), resp_text[1:])
    return data

zip_locs = DataFrame.from_csv('data/zip_names.csv',index_col='ZIP')
all_zips = zip_locs.index.tolist()

demographics = DataFrame()

for year in [2011, 2012]:
    year_demographics = DataFrame(columns=['ZIP', 'population'])
    for data_line in extractListFromURL('sf1', 'PCT0130001', year): #TOTAL POPULATION   P0010001 #POPULATION IN HOUSEHOUDS PCT0130001
        [population, junk, zip] = data_line
        if(zip in all_zips): year_demographics = year_demographics.append({'ZIP':zip, 'population':population}, ignore_index=True)
    year_demographics.index = map(int, year_demographics['ZIP'])

    SF1_KEYS = {'male':['PCT0130003', 'PCT0130004', 'PCT0130005', 'PCT0130006'],
                'female':['PCT0130027', 'PCT0130028', 'PCT0130029', 'PCT0130030']}
    year_demographics['population_over_18'] = year_demographics['population']
    for sex in ['female', 'male']:
        for sf1_var in SF1_KEYS[sex]:
            for data_line in extractListFromURL('sf1', sf1_var,year):
                [population, junk, zip] = data_line
                if(zip in all_zips):
                    year_demographics.loc[year_demographics.ZIP==zip, 'population_over_18'] = year_demographics.ix[zip]['population_over_18'] - population

    year_demographics['income'] = Series(repeat(0, shape(year_demographics)[0]), index=year_demographics.index)
    for data_line in extractListFromURL('acs5', 'B19301_001E',year):
        [income, zip] = data_line
        year_demographics.loc[year_demographics.ZIP==zip, 'income'] =income

    year_demographics['z_income'] = zscore(year_demographics.income)

    year_demographics['mbsa'] = Series(repeat(0, shape(year_demographics)[0]), index=year_demographics.index)
    for data_line in extractListFromURL('acs5', 'C24020_003E',year):
        [male_mbsa, zip] = data_line
        if(zip in all_zips): year_demographics.loc[year_demographics.ZIP==zip, 'mbsa'] = male_mbsa


    for data_line in extractListFromURL('acs5', 'C24020_039E',year):
        [female_mbsa, zip] = data_line
        if(zip in all_zips): year_demographics.loc[year_demographics.ZIP==zip, 'mbsa'] = year_demographics.ix[zip]['mbsa'] + female_mbsa

    year_demographics['mbsa'] = year_demographics['mbsa']/ map(float, year_demographics['population'])

    ACS_KEYS = {'male':['B23001_007E', 'B23001_014E', 'B23001_021E', 'B23001_028E', 'B23001_028E', 'B23001_035E', 'B23001_042E', 'B23001_049E',
                        'B23001_056E', 'B23001_063E', 'B23001_070E', 'B23001_075E', 'B23001_080E','B23001_085E'],
                'female':['B23001_093E','B23001_100E','B23001_107E','B23001_114E','B23001_121E','B23001_128E','B23001_135E',
                          'B23001_142E','B23001_149E','B23001_156E','B23001_161E','B23001_166E','B23001_171E']}

    zip_workforce_size = {}
    for sex in ['female', 'male']:
        for acs_var in ACS_KEYS[sex]:
            for data_line in extractListFromURL('acs5', acs_var,year):
                [value, zip] = data_line
                if(zip in all_zips): 
                    if(not zip_workforce_size.has_key(zip)):  zip_workforce_size[zip] = int(value)
                    else: zip_workforce_size[zip] +=  int(value)


    year_demographics['workforce'] = Series(repeat(0, shape(year_demographics)[0]), index=year_demographics.index)
    for zip, workforce_size in zip_workforce_size.iteritems():
        year_demographics.loc[year_demographics.ZIP==zip, 'workforce'] = workforce_size/float(year_demographics.ix[zip]['population'])

    year_demographics['mbsa_workforce'] = year_demographics['mbsa'] / year_demographics['workforce']
    year_demographics['z_mbsa_workforce'] = zscore(year_demographics['mbsa_workforce'])

    ACS_KEYS = {'female':{'ns':'B15002_020E', 'n4': 'B15002_021E', '5+6':'B15002_022E', '7+8':'B15002_023E',
                          '9':'B15002_024E', '10':'B15002_024E', '11':'B15002_025E', '12':'B15002_026E', 
                          'hs':'B15002_028E', 'sc1':'B15002_029E', 'sc2':'B15002_030E',
                          'aa':'B15002_031E', 'ba':'B15002_032E', 'ma':'B15002_033E', 
                          'pro':'B15002_034E','phd':'B15002_035E'},
                'male': {'ns':'B15002_003E', 'n4': 'B15002_004E', '5+6':'B15002_005E', '7+8':'B15002_006E',
                         '9':'B15002_007E', '10':'B15002_008E', '11':'B15002_009E', '12':'B15002_010E',
                         'hs':'B15002_011E', 'sc1':'B15002_012E', 'sc2':'B15002_013E',
                         'aa':'B15002_014E', 'ba':'B15002_015E', 'ma':'B15002_016E',
                         'pro':'B15002_017E', 'phd':'B15002_018E'} }
    zip_ed = {}
    for sex in ['female', 'male']:
        for ed_key, acs_var in ACS_KEYS[sex].iteritems():
            for data_line in extractListFromURL('acs5', acs_var, year):
                [value, zip] = data_line
                if(int(zip) in all_zips):   
                    if(not zip_ed.has_key(int(zip))):  zip_ed[int(zip)] = {sex+'_'+ed_key : int(value)}
                    else: zip_ed[int(zip)][sex+'_'+ed_key] = int(value)

    zip_ed_df = DataFrame(columns = ['ZIP'] + ACS_KEYS['female'].keys())
    for zip in all_zips:
        zip_total = {'ZIP':zip}
        for ed_key in ACS_KEYS['female'].keys():
            zip_total[ed_key] = (zip_ed[zip]['male_'+ed_key]+ zip_ed[zip]['female_'+ed_key]) / float(year_demographics.ix[zip]['population'])
        zip_ed_df = zip_ed_df.append( zip_total , ignore_index=True)
    zip_ed_df.index = map(int, zip_ed_df.ZIP)

    year_demographics = merge(zip_ed_df, year_demographics, on='ZIP')
    year_demographics.index = map(int, year_demographics.ZIP)

    year_demographics['education'] = (2.5*year_demographics['n4'] + 5.5*year_demographics['5+6'] + 7.5*year_demographics['7+8'] + 9*year_demographics['9'] + 10*year_demographics['10'] + 11*year_demographics['11'] + 12*year_demographics['12'] + 12*year_demographics['hs'] +13*year_demographics['sc1'] + 13*year_demographics['sc2'] +  14*year_demographics['aa'] + 16*year_demographics['ba'] + 18*year_demographics['ma'] + 18*year_demographics['pro'] + 18*year_demographics['phd']) 

    year_demographics['z_education'] = zscore(year_demographics['education'])

    year_demographics['ses'] = year_demographics['z_mbsa_workforce'] + year_demographics['z_income'] + year_demographics['z_education']

    year_demographics['desc'] = Series(repeat(0, shape(year_demographics)[0]), index=year_demographics.index)
    for zip in year_demographics.ZIP: 
        year_demographics.loc[year_demographics.ZIP==zip,'desc']= zip_locs.ix[int(zip)][0] + ':' + zip_locs.ix[int(zip)][1]

    year_demographics['year'] = repeat(year, shape(year_demographics)[0])

    if(len(demographics.columns)==0):
        demographics = year_demographics
    else:
        demographics = concat([demographics,year_demographics])

cPickle.dump(demographics, open('data/2011_2012_demographics.dat', 'wb'),1)

mean_demographics = demographics.groupby('ZIP').aggregate(mean)
mean_demographics.index = map(int, mean_demographics.index)
mean_demographics['ZIP'] = mean_demographics.index
mean_demographics['desc'] = Series(repeat(0, shape(mean_demographics)[0]), index=mean_demographics.index)
for zip in mean_demographics.ZIP: 
    mean_demographics.loc[mean_demographics.ZIP==zip,'desc']= zip_locs.ix[int(zip)][0] + ':' + zip_locs.ix[int(zip)][1]

cPickle.dump(mean_demographics, open('data/demographics.dat', 'wb'),1)

