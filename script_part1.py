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
print(measurements)

# work is committed


