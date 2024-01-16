# Part 1

#precipitation data (json file) is imported and opened

import json
from csv import DictReader

with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# Research on precipitation in Seattle
# manually the stations csv file is opened to obtain the station code for Seattle (GHCND:US1WAKG0038)
# precipitation file is a list of dictionaries
# a list of Seattle measurements is created and each Seattle measurement is added to it using the station code
# using a for loop, each measurement in the precipitation file is searched through for the Seattle station

#total monthly precipitation is calculated for each month by setting a count for each month and using a for loop to go through each measurement looking for the values of one months measurement

with open('stations.csv') as csvfile:
    stationsfile = DictReader(csvfile)
    stations = list(stationsfile)


for station in stations:
    station_code = station["Station"]
    station_location = station["Location"]
    station_state = station["State"]

    total_monthly = [0]*12
    Results = {}
    Results[station_location] = {}
    Results[station_location]["Station"] = station_code
    Results[station_location]["State"] = station_state
    relative_monthly = []
    
    for measurement in precipitation:
        month = measurement["date"]
        if measurement["station"] == station_code:
            for i in range(1,13):
                if i <10:
                    i = f'0{i}'
                if month.startswith(f'2010-{i}'):
                    total_monthly[int(i)-1] += measurement["value"]
                    total_yearly = sum(total_monthly)
        for item in total_monthly:
            relative_monthly_calculated= item/total_yearly
            relative_monthly.append(relative_monthly_calculated)
            Results[station_location]["total_monthly_precipitation"] = total_monthly
            Results[station_location]["total_yearly_precipitation"] = total_yearly
            Results[station_location]["relative_monthly_precipitation"] = relative_monthly
    print(Results)

# I was working on the relative monthly precipitation, but i keep getting an error message: ZeroDivisionError for item/total_yearly (which is weird cause they are both numbers and not zero)
# the dictionary created does create a dictionary, but it has not been written into a json file yet


