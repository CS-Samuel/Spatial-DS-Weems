"""
Program:
--------
    Program 4 - Query Assignments - Query 1: Find Interesting Features along some path:
    query1.py

Description:
------------
    Select a starting point: X and a destination point Y. This can be done by mouse click, or by entering airport codes via sys.argv 
    (e.g. python query1.py DFW MNL 500 to run query from Dallas / Fort Worth to Manilla Philippines with a 500 mile radius to look for interesting features).

    Determine a multi-line path between X & Y, and draw an appropriate line connecting each point.

    Highlight all features within R radius of the entire path by showing volcanos as red dots, earthquakes as blue dots, and meteor locations as green dots.

    Assume that each line segment cannot be more than 500 miles long, meaning you must find an airport within a 500 mile radius of each stop. 
    Choose the largest airport at each stop (e.g. where ap_level is the lowest value) and if there are more than one airport with the same ap_level, 
    choose the airport at the lowest elevation as a tie breaker.

    An example X and Y might be Dallas, U.S. to Manila, Philippines with a 500 mile radius.
    Which way do you fly to start? East or West?
    
Name: Samuel Weems
Date: 05 July 2017
"""


import pygame
import sys,os
import json
from mongo_helper_class import *
from mongo_helper import *
from draw import*


def same_continents_path (origin,destination,radius):
    mh = mongoHelper()
    airport_path = []
    airport_path.append(origin)
    airport_options = []
    

    x,y = airport_path[0]
    xfinal,yfinal = destination

    while (mh.haversine(y,x,yfinal,xfinal) > radius):

        distances_to_destination = []
        airport_options = mh.get_nearest_airports(x,y,radius)
    
        for airport in airport_options:
            x,y = airport 
            distances_to_destination.append(mh.haversine(yfinal,xfinal,y,x))
              
        airport_path.append(airport_options[(distances_to_destination.index(min(distances_to_destination)))])
               
        x,y = airport_path[(len(airport_path)-1)]

    airport_path.append(destination)
    return airport_path


def different_continents_path(origin,destination,radius,originContinent):
    mh = mongoHelper()
    airport_path = []
    airport_path.append(origin)
    airport_options = []
    
    global west_flag
    west_flag = False

    east_gateway = [-51.6781005859, 64.19090271]
    west_gateway = [-173.24299621582, 64.37809753418]
    
    xOrigin,yOrigin = airport_path[0]
    xFinal,yFinal = destination

    xWest, yWest = west_gateway
    xEast, yEast = east_gateway

    west_path = (mh.haversine(yFinal, xFinal, yWest, xWest)) + (mh.haversine(yOrigin, xOrigin, yWest, xWest))
    east_path = (mh.haversine(yFinal, xFinal, yEast, xEast)) + (mh.haversine(yOrigin, xOrigin, yEast, xEast))

    if (west_path < east_path):
        xGateway, yGateway = west_gateway
        gateway = west_gateway
        west_flag = True
               
    else:
        xGateway, yGateway = east_gateway
        gateway = east_gateway
    
    x,y = airport_path[0]
    
    while (mh.haversine(y,x,yGateway,xGateway) > radius):

        distances_to_destination = []
        airport_options = mh.get_nearest_airports(x,y,radius)
    
        for airport in airport_options:
            x,y = airport 
            distances_to_destination.append(mh.haversine(yGateway,xGateway,y,x))
              
        airport_path.append(airport_options[(distances_to_destination.index(min(distances_to_destination)))])
               
        x,y = airport_path[(len(airport_path)-1)]

    airport_path.append(gateway)

    x,y = gateway

    while (mh.haversine(y,x,yFinal,xFinal) > radius):

        distances_to_destination = []
        airport_options = mh.get_nearest_airports(x,y,radius)
    
        for airport in airport_options:
            x,y = airport 
            distances_to_destination.append(mh.haversine(yFinal,xFinal,y,x))
              
        airport_path.append(airport_options[(distances_to_destination.index(min(distances_to_destination)))])
               
        x,y = airport_path[(len(airport_path)-1)]

    airport_path.append(destination)
    
    return airport_path



# Get current working path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':
    
    mh = mongoHelper()
    mh2 = MongoHelper()
    airport_radius = 1200
    airport_path = []
    
    airport_origin_code = sys.argv[1]
    airport_destination_code = sys.argv[2]
    feature_radius = sys.argv[3]

    airport_origin_coordinates = mh.get_airport_coordinates(airport_origin_code)
    airport_destination_coordinates = mh.get_airport_coordinates(airport_destination_code)

    volcanos = []
    tempVolcanos = []
    earthquakes = []
    tempEarthquakes = []
    meteors = []
    tempMeteors = []
    

    west_gateway = [-173.24299621582, 64.37809753418]
    west_extreme = -180
    east_extreme = 180

    west_flag = False

# Check for continent locations for routing

    airport_origin_continent = mh.get_airport_continent(airport_origin_code)
    airport_destination_continent = mh.get_airport_continent(airport_destination_code)

    if (airport_origin_continent == 'Americas' or airport_destination_continent == 'Americas'):
        if (airport_origin_continent == 'Americas' and airport_destination_continent == 'Americas'):
            airport_path = same_continents_path(airport_origin_coordinates, airport_destination_coordinates, airport_radius)
        else:
            airport_path = different_continents_path(airport_origin_coordinates, airport_destination_coordinates, airport_radius, airport_origin_continent)
    else:
        airport_path = same_continents_path(airport_origin_coordinates, airport_destination_coordinates, airport_radius)


#Find features within R radius of each airport

for point in airport_path:
    tempVolcanos.append(mh2.get_features_near_me("volcanos", point, float(feature_radius)))
    tempEarthquakes.append(mh2.get_features_near_me("earthquakes", point, float(feature_radius)))
    tempMeteors.append(mh2.get_features_near_me("meteorites", point, float(feature_radius)))

    for i in range(len(tempVolcanos[0])-1):
        volcanos.append(tempVolcanos[0][i])
    for i in range(len(tempEarthquakes[0])-1):
        earthquakes.append(tempEarthquakes[0][i])
    for i in range(len(tempMeteors[0])-1):
        meteors.append(tempMeteors[0][i])
    
    tempVolcanos = []
    tempEarthquakes = []
    tempMeteors = []



 # Display

screen_width = 2048
screen_height = 1024

mf = MapFacade(screen_width,screen_height)



#display volcanos as red dots, earthquakes as blue dots, and meteor locations as green dots.
    
mf.pyg.add_points(volcanos,map_icon('Centered','Pink',16,''))
mf.pyg.add_points(earthquakes,map_icon('Centered','Azure',16,''))
mf.pyg.add_points(meteors,map_icon('Centered','Chartreuse',16,''))

#draw line flight path
if (west_flag == False):
    mf.pyg.add_path(airport_path)
else:
    path1 = []
    path2 = []

    index = airport_path.index(west_gateway)
    
    if (airport_origin_continent == 'Americas'):
        for i in range(index+1):
            path1.append(airport_path[i])
        for i in range(index+2, len(airport_path)):
            path2.append(airport_path[i])
        
        x,y = west_gateway
        x = west_extreme
        path1.append([x,y])

        x,y = path2[0]
        x = east_extreme
        path2.insert(0,[x,y])          

    else:
        for i in range(index):
            path1.append(airport_path[i])
        for i in range(index, len(airport_path)):
            path2.append(airport_path[i])

        x,y = path1[len(path1)-1]
        x = east_extreme
        path1.append([x,y])

        x,y = path2[0]
        x = west_extreme
        path2.insert(0,[x,y])
   

    mf.pyg.add_path(path1)
    mf.pyg.add_path_2(path2)

#display flight path points
mf.pyg.add_points(airport_path,map_icon('Centered','Pink',32,''))
    
    #py query1.py MNL DFW 500
    #C:\Users\Admin\OneDrive\4553-Spatial-DS\Spatial-DS-Weems\Assignments\program_5


#mf.pin_the_map( [[131.6,34.5],[140.29,37.64],[139.2,36.56]],map_icon('Centered','Pink',32,''))
#mf.pin_the_map([[-98.5034180,33.9382331]],map_icon('Centered','Pink',32,''))
# mf.draw_country('BRA')
# mf.draw_country('GRL')
# mf.draw_country('RUS')
# mf.draw_country('FRA',(199,21,133),0)
# mf.draw_country('NOR',(21,199,133),0)

#mf.draw_airports(map_icon('Centered','Azure',16,''))

mf.run()



