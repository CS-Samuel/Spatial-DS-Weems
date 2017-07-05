"""
Program:
--------
    Program 4 - Query Assignments - Query 2: Nearest Neighbor
    nearest_neighbor.py

Description:
------------
    Click on the world map and get the nearest feature within XXX miles, possibly with specific feature values, 
    further filtering the query (magnitude of earthquake, etc.) where features are listed below:
        Volcanos
        Earthquakes
        Meteors

    Example queries may be:
        python query2.py [feature] [field] [field value] [min/max] [max results] [radius] [lon,lat]
            feature = volcano, earthquake, meteor
            field = some field in the 'properties' to compare against
            field_value = the value in wich to compare with
            min/max = whether we want all results greater than or less than the field_value.
            radius (in miles) = radius to apply our query with.
            lon,lat (optional) = Some point coords to act as a mouse click instead of actually clicking the screen. If these exist when query2.py is run, then it should just perform the query with the given point and not wait on a mouse click.

    python query2.py volcanos altitude 3000 min 3 1000 
    When the map is clicked it will find the 3 volcanos within a 1000 mile radius that are at a minumum of 3000 feet (if they exist at that location).

    python query2.py earthquakes magnitude 5 min 0 2000 
    When the map is clicked it will find ALL earthquakes (max results 0 = all) within a 2000 mile radius with a magnitude of 5 or more.

    python query2.py 1000 
    This query if rum with a single parameter, you will assume it is a Radius and you should find ALL of the above features within that radius
    (Volcanos, Earthquakes, Meteors). Only display the first 500 results if there are any performance issues.

    Show volcanos as red dots, earthquakes as blue dots, and meteor locations as green dots.

Name: Samuel Weems
Date: 05 July 2017
"""

import pygame
import sys,os
import json
from mongo_helper_class import *
from mongo_helper import *
from draw import*


# Get current working path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

def mercToLL(point):
    lng,lat = point
    lng = lng / 256.0 * 360.0 - 180.0
    n = math.pi - 2.0 * math.pi * lat / 256.0
    lat = (180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n))))
    return (lng, lat)
    

def toLL(point):
    ans = []
    x,y = point
    y += 256
    return mercToLL((x/4,y/4))


if __name__ == '__main__':

# Display and get click point

    

    screen_width = 1024
    screen_height = 512
    mf = MapFacade(screen_width,screen_height)

    if (len(sys.argv) < 6):
        radius = sys.argv[1]
        feature = "all"
        click_point = mf.run()
        point = toLL((click_point))

        if (len(sys.argv) == 3):
            input_point = sys.argv[2]
            
        
    else:
        feature = sys.argv[1]
        field = sys.argv[2]
        min_max_value = sys.argv[3]
        min_max = sys.argv[4]
        max_results = sys.argv[5]
        radius = sys.argv[6]
        click_point = mf.run()
        point = toLL((click_point))
        if (len(sys.argv) == 8):
            input_point = sys.argv[7]
            
    
    
    if (len(sys.argv) == 8 or len(sys.argv) == 3):
        x,y = input_point.split(',')
        x= float(x)
        y= float(y)
        point = ([x,y])
        
   
    mh2 = MongoHelper()

    volcanos = []
    earthquakes = []
    meteors = []

    tempVolcanos = []
    tempEarthquakes =[]
    tempMeteors = []

    tempFeatures = []
    features = []
  
    







# lat,lon = toLL((click_point))
# point = ([lon,lat])

#Find features

#point = [-97.03800201416, 32.896800994873]

if (feature == "all"):


    tempVolcanos.append(mh2.get_features_near_me("volcanos", point, float(radius)))
    tempEarthquakes.append(mh2.get_features_near_me("earthquakes", point, float(radius)))    
    tempMeteors.append(mh2.get_features_near_me("meteorites", point, float(radius)))

    for i in range(len(tempVolcanos[0])-1):
        volcanos.append(tempVolcanos[0][i])
    for i in range(len(tempEarthquakes[0])-1):
        earthquakes.append(tempEarthquakes[0][i])
    for i in range(len(tempMeteors[0])-1):
        meteors.append(tempMeteors[0][i])
    

    if (volcanos):
        mf.pyg.add_points(volcanos,map_icon('Centered','Pink',16,''))
    if (earthquakes):
        mf.pyg.add_points(earthquakes,map_icon('Centered','Azure',16,''))
    if (meteors):
        mf.pyg.add_points(meteors,map_icon('Centered','Chartreuse',16,''))

else:
    if (field == "magnitude"):
        tempFeatures.append(mh2.get_features_limited_near_me("earthquakes", "mag", min_max, min_max_value, point, radius))
        feature_color = "Azure"

    if (field == "altitude"):
        tempFeatures.append(mh2.get_features_limited_near_me("volcanos", "Altitude", min_max, min_max_value, point, radius))
        feature_color = "Pink"

    if (field == "mass"):
        tempFeatures.append(mh2.get_features_limited_near_me("meteorites", "mass", min_max, min_max_value, point, radius))
        feature_color = "Chartreuse"

    
    
    if (int(max_results) == 0):
        if (tempFeatures[0]):
            for i in range(len(tempFeatures[0])-1):
                features.append(tempFeatures[0][i])
            mf.pyg.add_points(features,map_icon('Centered', feature_color,16,''))
    else:
        if (tempFeatures[0]):
            for i in range(int(max_results)-1):
                features.append(tempFeatures[0][i])
            mf.pyg.add_points(features,map_icon('Centered', feature_color,16,''))
       

mf.run()

        
 
    