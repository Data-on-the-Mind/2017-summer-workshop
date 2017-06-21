import re

#download and uncompress the pluto datafiles (https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nyc_pluto_11v2.zip  ) to this directory:
DATA_PATH = 'data/nyc_pluto_11v2'

zoning = DataFrame() 

for boro in ['bk', 'mn', 'si', 'bx', 'qn']:
    pluto_file = DATA_PATH+'/'+boro+'11v2.txt'
    print 'loading:', pluto_file
    burough_zoning = DataFrame.from_csv(pluto_file, index_col = 'Block')

    zips = map(int, filter(lambda x:re.match(r'[0-9]', str(x), re.M|re.I), burough_zoning.ZipCode.unique()))
    zips = filter(lambda x:x in demographics.ZIP, zips)

    grouped = burough_zoning.groupby('ZipCode')

    burough_df = DataFrame(columns = ['ZIP', 'num_residential', 'num_total'])

    for zip, zip_zoning in grouped:
        if(not zip.isdigit()): continue
        zonedist1 = zip_zoning.AllZoning1.tolist()
        
        if(int(zip) in zips):
            zip_row = {'ZIP':int(zip),
                       'num_residential':len(filter(lambda x:re.match( r'R[0-9]', x, re.M|re.I), 
                                                    map(lambda x:str(x).strip(), zonedist1))),
                       'num_total':len(zonedist1)}

            burough_df = burough_df.append ( zip_row ,ignore_index=True)
        else:
            print 'not in demographics:',zip
        
    zoning = concat([zoning, burough_df])

for zip in zoning.ZIP:
    if(zoning.ZIP.tolist().count(zip) > 1):
        dupe_zips = zoning[zoning.ZIP==zip]
        zoning = zoning[zoning.ZIP != zip]
        zip_row = {'ZIP':zip}
        for col in filter(lambda x:x != 'ZIP', dupe_zips.columns):
            zip_row[col] = sum(dupe_zips[col])
        print zip_row
        zoning = zoning.append(zip_row, ignore_index=True)

zoning.index = zoning.ZIP.astype(int)

for zip in zoning.ZIP:
    if(zip not in demographics.ZIP):
        print 'demographics missing zip:', zip

for zip in demographics.index:
    if(zip not in zoning.index):
        print 'zoning missing zip:', zip


zoning['prop_residential'] = zoning.num_residential.astype(float) / zoning.num_total
cPickle.dump(zoning, open('data/zoning.dat', 'wb'))
