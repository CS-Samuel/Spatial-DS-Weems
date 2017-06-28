"""
Program:
--------
    Program 4 - GeoJson
    generate_city_locations_geojson.py

Description:
------------
    This program formats data into GeoJson output
    
Name: Samuel Weems
Date: 28 June 2017
"""

import os,sys
import json
import collections

#Current Working Path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

file = open('world_cities_large.json', 'r')

data = file.read()
data = json.loads(data)

all_cities = []



for k,v in data.items():
    for i in range (len(v)):
        entry = collections.OrderedDict()
        entry['type'] = "Feature"
        entry['properties'] = v[i]
        lat = float(v[i]['lat'])
        lon = float(v[i]['lon'])
        del entry['properties']['lat']
        del entry['properties']['lon']
        entry["geometry"] = {}
        entry["geometry"]["type"]="Point"
        entry["geometry"]["coordinates"] = [lon,lat]
       
        all_cities.append(entry)


#Limits output to first 1000 entries
del all_cities [999: len(all_cities)-1]

output = open(DIRPATH+'/geo_json/1k_cities_geo_json.geojson', 'w')
output.write(json.dumps(all_cities, sort_keys=False,indent=4, separators=(',', ': ')))
output.close()