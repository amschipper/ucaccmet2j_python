# Part 1

#precipitation data (json file) is imported and opened

import json

with open('precipitation.json', encoding='utf-8') as file:
    precipitation = json.load(file)

# Research on precipitation in Seattle
# manually the stations csv file is opened to obtain the station code for Seattle (GHCND:US1WAKG0038)
# precipitation file is a list of dictionaries
# a list of Seattle measurements is created and each Seattle measurement is added to it using the station code
# using a for loop, each measurement in the precipitation file is searched through for the Seattle station

measurements = []
for measurement in precipitation:
    station = measurement["station"]
    if station == "GHCND:US1WAKG0038":
        measurements.append(measurement["value"])

# work is committed

#total monthly precipitation is calculated for each month by setting a count for each month and using a for loop to go through each measurement looking for the values of one months measurement

total_january_precipiation_Seattle = 0
total_january_precipitation_Cincinatti = 0
total_january_precipiation_Maui = 0
total_january_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-01"):
        total_january_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-01"):
        total_january_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-01"):
        total_january_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-01"):
        total_january_precipitation_San_Diego += measurement["value"]
print(total_january_precipiation_Seattle)
print(total_january_precipitation_Cincinatti)
print(total_january_precipiation_Maui)
print(total_january_precipitation_San_Diego)

total_february_precipiation_Seattle = 0
total_february_precipitation_Cincinatti = 0
total_february_precipiation_Maui = 0
total_february_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-02"):
        total_february_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-02"):
        total_february_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-02"):
        total_february_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-02"):
        total_february_precipitation_San_Diego += measurement["value"]

total_march_precipiation_Seattle = 0
total_march_precipitation_Cincinatti = 0
total_march_precipiation_Maui = 0
total_march_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-03"):
        total_march_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-03"):
        total_march_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-03"):
        total_march_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-03"):
        total_march_precipitation_San_Diego += measurement["value"]

total_april_precipiation_Seattle = 0
total_april_precipitation_Cincinatti = 0
total_april_precipiation_Maui = 0
total_april_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-04"):
        total_april_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-04"):
        total_april_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-04"):
        total_april_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-04"):
        total_april_precipitation_San_Diego += measurement["value"]

total_may_precipiation_Seattle = 0
total_may_precipitation_Cincinatti = 0
total_may_precipiation_Maui = 0
total_may_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-05"):
        total_may_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-05"):
        total_may_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-05"):
        total_may_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-05"):
        total_may_precipitation_San_Diego += measurement["value"]

total_june_precipiation_Seattle = 0
total_june_precipitation_Cincinatti = 0
total_june_precipiation_Maui = 0
total_june_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-06"):
        total_june_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-06"):
        total_june_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-06"):
        total_june_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-06"):
        total_june_precipitation_San_Diego += measurement["value"]

total_july_precipiation_Seattle = 0
total_july_precipitation_Cincinatti = 0
total_july_precipiation_Maui = 0
total_july_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-07"):
        total_july_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-07"):
        total_july_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-07"):
        total_july_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-07"):
        total_july_precipitation_San_Diego += measurement["value"]

total_august_precipiation_Seattle = 0
total_august_precipitation_Cincinatti = 0
total_august_precipiation_Maui = 0
total_august_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-08"):
        total_august_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-08"):
        total_august_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-08"):
        total_august_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-08"):
        total_august_precipitation_San_Diego += measurement["value"]

total_september_precipiation_Seattle = 0
total_september_precipitation_Cincinatti = 0
total_september_precipiation_Maui = 0
total_september_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-09"):
        total_september_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-09"):
        total_september_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-09"):
        total_september_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-09"):
        total_september_precipitation_San_Diego += measurement["value"]

total_october_precipiation_Seattle = 0
total_october_precipitation_Cincinatti = 0
total_october_precipiation_Maui = 0
total_october_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-10"):
        total_october_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-10"):
        total_october_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-10"):
        total_october_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-10"):
        total_october_precipitation_San_Diego += measurement["value"]

total_november_precipiation_Seattle = 0
total_november_precipitation_Cincinatti = 0
total_november_precipiation_Maui = 0
total_november_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-11"):
        total_november_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-11"):
        total_november_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-11"):
        total_november_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-11"):
        total_november_precipitation_San_Diego += measurement["value"]

total_december_precipiation_Seattle = 0
total_december_precipitation_Cincinatti = 0
total_december_precipiation_Maui = 0
total_december_precipitation_San_Diego = 0
for measurement in precipitation:
    station = measurement["station"]
    month = measurement["date"]
    if station =="GHCND:US1WAKG0038" and month.startswith("2010-12"):
        total_december_precipiation_Seattle += measurement["value"]
    if station == "GHCND:USW00093814" and month.startswith("2010-12"):
        total_december_precipitation_Cincinatti += measurement["value"]
    if station == "GHCND:USC00513317" and month.startswith("2010-12"):
        total_december_precipiation_Maui += measurement["value"]
    if station == "GHCND:US1CASD0032" and month.startswith("2010-12"):
        total_december_precipitation_San_Diego += measurement["value"]


# # an empty list is created for the total monthly precipitation, and each individual total value for a month is added to the list

total_monthly_precipitation_Seattle = []
total_monthly_precipitation_Cincinatti = []
total_monthly_precipitation_Maui = []
total_monthly_precipitation_San_Diego = []

total_monthly_precipitation_Seattle.append(total_january_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_february_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_march_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_april_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_may_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_june_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_july_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_august_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_september_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_october_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_november_precipiation_Seattle)
total_monthly_precipitation_Seattle.append(total_december_precipiation_Seattle)

total_monthly_precipitation_Cincinatti.append(total_january_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_february_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_march_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_april_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_may_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_june_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_july_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_august_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_september_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_october_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_november_precipitation_Cincinatti)
total_monthly_precipitation_Cincinatti.append(total_december_precipitation_Cincinatti)

total_monthly_precipitation_Maui.append(total_january_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_february_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_march_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_april_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_may_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_june_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_july_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_august_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_september_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_october_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_november_precipiation_Maui)
total_monthly_precipitation_Maui.append(total_december_precipiation_Maui)

total_monthly_precipitation_San_Diego.append(total_january_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_february_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_march_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_april_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_may_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_june_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_july_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_august_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_september_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_october_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_november_precipitation_San_Diego)
total_monthly_precipitation_San_Diego.append(total_december_precipitation_San_Diego)

# # All characteristics of Seattle are put into a new dictionary titled Seattle, including the gotten results on the precipitation and written into a new json file for results and indented at 4 to give it a nice overview

Seattle = {}
Seattle["station"] = "GHCND:US1WAKG0038"
Seattle["state"] = "WA"
Seattle["total_monthly_precipitation"] = total_monthly_precipitation_Seattle
Results = {}
Results["Seattle"] = Seattle

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Results, file, indent=4)

# # Part 2
    
# # yearly precipitation is calculated by summing all the totals of the individual months

total_yearly_precipitation_Seattle = 0
total_yearly_precipitation_Cincinatti= 0
total_yearly_precipitation_Maui = 0
total_yearly_precipitation_San_Diego = 0
for total_month in total_monthly_precipitation_Seattle:
    total_yearly_precipitation_Seattle += total_month
for total_month in total_monthly_precipitation_Cincinatti:
    total_yearly_precipitation_Cincinatti += total_month
for total_month in total_monthly_precipitation_Maui:
    total_yearly_precipitation_Maui += total_month
for total_month in total_monthly_precipitation_San_Diego:
    total_yearly_precipitation_San_Diego += total_month

Seattle["total_yearly_precipitation"] = total_yearly_precipitation_Seattle

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Results, file, indent=4)

# # relative monthly precipitation is calculated using the total per month and the total of the year

relative_january_precipitation = total_january_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_february_precipitation = total_february_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_march_precipitation = total_march_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_april_precipitation = total_april_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_may_precipitation = total_may_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_june_precipitation = total_june_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_july_precipitation = total_july_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_august_precipitation = total_august_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_september_precipitation = total_september_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_october_precipitation = total_october_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_november_precipitation = total_november_precipiation_Seattle/total_yearly_precipitation_Seattle
relative_december_precipitation = total_december_precipiation_Seattle/total_yearly_precipitation_Seattle

# # a list is created for the relative monthly values and the relative values are added per month

relative_monthly_precipitation = []
relative_monthly_precipitation.append(relative_january_precipitation)
relative_monthly_precipitation.append(relative_february_precipitation)
relative_monthly_precipitation.append(relative_march_precipitation)
relative_monthly_precipitation.append(relative_april_precipitation)
relative_monthly_precipitation.append(relative_may_precipitation)
relative_monthly_precipitation.append(relative_june_precipitation)
relative_monthly_precipitation.append(relative_july_precipitation)
relative_monthly_precipitation.append(relative_august_precipitation)
relative_monthly_precipitation.append(relative_september_precipitation)
relative_monthly_precipitation.append(relative_october_precipitation)
relative_monthly_precipitation.append(relative_november_precipitation)
relative_monthly_precipitation.append(relative_december_precipitation)

# # dictionary key is added for the relative monthly precipitation and added to the results json file

Seattle["relative_monthly_precipitation"] = relative_monthly_precipitation

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Results, file, indent=4)

# # Part 3

# In the code above all has been adapted to be calculated (necessary parts) to have it for all cities. 
    
# To calculate relative yearly precipitation, we need the yearly precipitation of Seattle and all the yearly precipitation added up
    
total_yearly_all = (total_yearly_precipitation_Seattle + total_yearly_precipitation_Cincinatti + total_yearly_precipitation_Maui + total_yearly_precipitation_San_Diego)
print(total_yearly_all)

relative_yearly_precipitation = total_yearly_precipitation_Seattle/total_yearly_all
print(relative_yearly_precipitation)

# we create a new key in the results json file to add the relative yearly precipitation to the results
Seattle["relative_yearly_precipitation"] = relative_yearly_precipitation

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Results, file, indent=4)

# I thought the assignment was just to make a json file on Seattle, and not add all the information for all the locations to the json file. I could have done that with my code, but no time.

