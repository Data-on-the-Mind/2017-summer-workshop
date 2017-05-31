mean_lott = lott.groupby('date').aggregate(mean)

figure()
subplot(211)
for ZIP in [10003,11234,11238]:
    lott[lott.ZIP==ZIP].composite.plot(label=str(ZIP) + ':'+demographics.ix[ZIP]['desc'])
ylabel('ZIP composite gambling ($/day')
xlabel('date')
legend()


subplot(212)
for ZIP in [10003,11234,11238]:
    lott[lott.ZIP==ZIP].composite_per_capita.plot(label=str(ZIP) + ':'+demographics.ix[ZIP]['desc'])
ylabel('ZIP per capita gambling ($/person/day')
xlabel('date')
legend()
show()


figure()
mean_lott.composite_per_capita.plot()
ylabel('citywide composite per capita gambling ($/person/day')
xlabel('date')
show()

