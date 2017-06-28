"""
Program:
--------
    Program 4 - GeoJson
    generate_earthquakes_geojson.py

Description:
------------
    This program formats data into GeoJson output

    The earthquakes file is already formated for GeoJson so this program outputs only 1,000 objects for upload to GitHub
    
Name: Samuel Weems
Date: 28 June 2017
"""


import os,sys
import json


#Current Working Path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

file = open('quake-2017.json', 'r')

data = file.read()


data = json.loads(data)

#Limits output to first 1000 entries
del data [999: len(data)-1]
  
output = open(DIRPATH+'/geo_json/1k_earthquakes_geo_json.geojson', 'w')
output.write(json.dumps(data, sort_keys=False,indent=4, separators=(',', ': ')))
output.close()