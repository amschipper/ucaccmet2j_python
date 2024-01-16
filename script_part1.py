# precipitatio data (json file) is imported and opened

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

total_january_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-01"):
        total_january_precipiation += measurement["value"]

total_february_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-02"):
        total_february_precipiation += measurement["value"]

total_march_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-03"):
        total_march_precipiation += measurement["value"]

total_april_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-04"):
        total_april_precipiation += measurement["value"]

total_may_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-05"):
        total_may_precipiation += measurement["value"]

total_june_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-06"):
        total_june_precipiation += measurement["value"]

total_july_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-07"):
        total_july_precipiation += measurement["value"]

total_august_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-08"):
        total_august_precipiation += measurement["value"]

total_september_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-09"):
        total_september_precipiation += measurement["value"]

total_october_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-10"):
        total_october_precipiation += measurement["value"]

total_november_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-11"):
        total_november_precipiation += measurement["value"]

total_december_precipiation = 0
for measurement in precipitation:
    month = measurement["date"]
    if month.startswith("2010-12"):
        total_december_precipiation += measurement["value"]

# an empty list is created for the total monthly precipitation, and each individual total value for a month is added to the list

total_monthly_precipitation = []
total_monthly_precipitation.append(total_january_precipiation)
total_monthly_precipitation.append(total_february_precipiation)
total_monthly_precipitation.append(total_march_precipiation)
total_monthly_precipitation.append(total_april_precipiation)
total_monthly_precipitation.append(total_may_precipiation)
total_monthly_precipitation.append(total_june_precipiation)
total_monthly_precipitation.append(total_july_precipiation)
total_monthly_precipitation.append(total_august_precipiation)
total_monthly_precipitation.append(total_september_precipiation)
total_monthly_precipitation.append(total_october_precipiation)
total_monthly_precipitation.append(total_november_precipiation)
total_monthly_precipitation.append(total_december_precipiation)

print(total_monthly_precipitation)

# All characteristics of Seattle are put into a new dictionary titled Seattle, including the gotten results on the precipitation and written into a new json file for results and indented at 4 to give it a nice overview

Seattle = {}
Seattle["station"] = "GHCND:US1WAKG0038"
Seattle["state"] = "WA"
Seattle["total_monthly_precipitation"] = total_monthly_precipitation
Results = {}
Results["Seattle"] = Seattle

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(Results, file, indent=4)

