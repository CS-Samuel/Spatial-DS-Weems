"""
Program:
--------
    Program 4 - Query Assignments - Query 3: Clustering
    query3.py

Description:
------------
    Use dbscan to find the top 3-5 clusters of volcanoes, earthquakes, and meteors.

    If combining all of the data points is hard, get the biggest cluster from each data type seperately.

    Draw a bounding box around each cluster.

    Example Usage may be:
        python query3.py [feature] [min_pts] [eps]
        
        Feature = (volcano, earthquake, meteor) and
        min_pts = minimum points to make a cluster, and
        eps is the distance parameter for dbscan

        python query3.py [feature] [min_pts] [eps]

Name: Samuel Weems
Date: 03 July 2017
"""

import pygame
import sys,os
import json
from mongo_helper_class import *
from mongo_helper import *
from draw import*
from dbscan import*
import pprint as pp

# Get current working path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':

    screen_width = 2048
    screen_height = 1024

    mh2 = MongoHelper()
    mf = MapFacade(screen_width,screen_height)

    feature = sys.argv[1]
    min_pts = sys.argv[2]
    epsilon = sys.argv[3]

    tempVolcanos = []
    tempEathquakes = []
    tempMeteors = []

    features = []
    clusters = []
    
    xvalues = []
    yvalues = []
    bounding_box = []
    polygon = []

    white = (255,255,255)


if (feature == "volcano"):
    features = mh2.get_all("volcanos")
    feature_color = "Pink"
    pp.pprint (features)
    
    
if (feature == "earthquake"):
    features = mh2.get_all("earthquakes")
    feature_color = "Azure"
    pp.pprint (features)
    

if (feature == "meteor"):
    features = mh2.get_all("meteorites")
    feature_color = "Chartreuse"
    pp.pprint (features)
    

clusters = dbscan(features, epsilon, int(min_pts))

counter = 0
if (len(clusters) > 1):
    for k in sorted(clusters, key=lambda k: len(clusters[k]), reverse=True):
        if (counter > 0 and counter < 6):
            if (clusters[k]):
                mf.pyg.add_points(clusters[k],map_icon('Centered',feature_color,16,''))
                for i in range (len (clusters[k])):
                    x,y = clusters[k][i]
                    xvalues.append(x)
                    yvalues.append(y)
                xmin = min(xvalues)
                ymin = min(yvalues)
                xmax = max(xvalues)
                ymax = max(yvalues)
                bounding_box.append([xmin,ymax])
                bounding_box.append([xmax,ymax])
                bounding_box.append([xmax,ymin])
                bounding_box.append([xmin,ymin])
                bounding_box.append([xmin,ymax])
                polygon.append(bounding_box)
                mf.pyg.add_polygon(polygon, white, 4)
                xvalues =[]
                yvalues =[]
                bounding_box = []
                polygon = []
        counter += 1

mf.run()



