"""
Program:
--------
    Program 4 - GeoJson
    generate_volcanos_geojson.py

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

file = open('world_volcanos.json', 'r')

data = file.read()
data = json.loads(data)

all_volcanos = []



for i in range (len(data)):
    
    if data[i]['Lat'] != "":
        entry = collections.OrderedDict()
        entry['type'] = "Feature"
        entry['properties'] = data[i]
        lat = float(data[i]['Lat'])
        lon = float(data[i]['Lon'])
        del entry['properties']['Lat']
        del entry['properties']['Lon']
        entry["geometry"] = {}
        entry["geometry"]["type"]="Point"
        entry["geometry"]["coordinates"] = [lon,lat]
       
        all_volcanos.append(entry)


#Limits output to first 1000 entries
del all_volcanos [999: len(all_volcanos)-1]

output = open(DIRPATH+'/geo_json/1k_volcanos_geo_json.geojson', 'w')
output.write(json.dumps(all_volcanos, sort_keys=False,indent=4, separators=(',', ': ')))
output.close()
