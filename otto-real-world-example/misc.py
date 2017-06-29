    
solar = DataFrame.from_csv('data/weather/solar_irradiance_' +str(ANALYSIS_YEAR) + '.csv')
solar['date'] = solar.index
solar['time'] = map(lambda x:time.strptime(x, "%H:%M").tm_hour, solar['Time (HH:MM)'])

sunshine = DataFrame({'dni': solar[logical_and(~isnan(solar.dni), solar.dni != 0)].groupby('date').mean()['dni']})

avg_dni = mean(sunshine['dni'])
for date in sunshine.index:
    if(not isnan(sunshine.ix[date]['dni'])):
        dni_pe = (sunshine.ix[date]['dni'] - avg_dni)
        avg_dni += 0.1*dni_pe
        sunshine.set_value(date, 'dni_exp_avg', avg_dni)
        sunshine.set_value(date, 'dni_pe', dni_pe)
    else:
        sunshine.set_value(date, 'dni_exp_avg', avg_dni)
        sunshine.set_value(date, 'dni_pe', nan)




weather = DataFrame.from_csv('data/weather/weather.csv', index_col='EST')
weather = weather[weather.index.year == ANALYSIS_YEAR]
storm_regressor = Series(data=zeros(len(analysis_range)),index=analysis_range)
storm_regressor.ix[ weather[logical_and(map(lambda x:'Snow' in str(weather.Events.ix[x]), weather.index), 
                                        weather.MeanVisibilityMiles < 5)].index.tolist() ] = 1



days_of_week_regressors = DataFrame(index=analysis_range)
for day_of_week in range(7):
    days_of_week_regressors[datetools.DAYS[day_of_week]] = map(int, analysis_range.dayofweek==day_of_week)

month_of_year_regressors = DataFrame(index=analysis_range)
for month_of_year in range(1,13):
    month_of_year_regressors[datetools.MONTHS[month_of_year-1]] = map(int, analysis_range.month==month_of_year)


