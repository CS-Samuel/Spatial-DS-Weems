"""
Program:
--------
    Program 4 - GeoJson
    generate_states_geojson.py

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

file = open('state_borders.json', 'r')

data = file.read()
data = json.loads(data)

all_states = []



for i in range (len(data)):
    
    entry = collections.OrderedDict()
    entry['type'] = "Feature"
    entry['properties'] = data[i]
    entry["geometry"] = {}
    if len(data[i]['borders']) == 1:
        entry["geometry"]["type"]="Polygon"
    else:
        entry["geometry"]["type"] = "MultiPolygon"
    entry["geometry"]["coordinates"] = data[i]['borders']
    del entry['properties']['borders']
         
    all_states.append(entry)


#Limits output to first 1000 entries
del all_states [999: len(all_states)-1]

output = open(DIRPATH+'/geo_json/1k_states_geo_json.geojson', 'w')
output.write(json.dumps(all_states, sort_keys=False,indent=4, separators=(',', ': ')))
output.close()

