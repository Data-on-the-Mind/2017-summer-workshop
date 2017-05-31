figure()
[x, y] = [[],[]]
grouped = lott.groupby('ZIP') 
for zip, zip_lott in grouped:
    zip_x = demographics.ix[zip]['ses']

#    zip_y = zip_lott.composite_per_capita.mean() #zip_lott['resid'].mean()    #
    zip_y =  (zip_lott['composite_per_capita'].sum() / demographics.ix[zip]['income'])*100.
#    zip_x = demographics.ix[zip]['prop_residential']
#    zip_y = max(lott[lott.ZIP == zip].RetailerCount) / demographics.ix[zip]['population_over_18']

    x.append(zip_x)
    y.append(zip_y)
    
    
[m, b, r, p, std_err] = linregress(x,y)
print 'r= '+str(r), 'p:', p
plot( [min(x), max(x)], b + m*array([min(x), max(x)]))
scatter(x,y) #,marker='+',s=30,color='black')
show()
