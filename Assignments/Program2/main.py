"""
Program:
--------
    Program 2 - DBScan Part 1

Description:
------------
    This program accesses crime data files from New York City. It gets the data points and then adjusts them for screen display.
    It creates a 2D scatterpolot of locations of crimes and color codes each point according to the 5 boroughs of NY.
    
Name: Samuel Weems
Date: 19 June 2017
"""

import pygame
import random
from dbscan import *
import sys,os
import pprint as pp

def getPoints (fileName, screenWidth, screenHeight):
    """Retrieves points from file and adjusts them for screen display

      Args:
        fileName: name of the file to retrieve data from
        screenWidth: width of display screen
        screenHeight: height of display screen

    Returns:
        A list of tuples containing points for screen projection

        
    """
    maxx = float(1067226) # The max coords from the 
    maxy = float(271820)  # whole file
    minx = float(913357)
    miny = float(121250)
    deltax = float(maxx) - float(minx)
    deltay = float(maxy) - float(miny)
    
    # Get current working path
    DIRPATH = os.path.dirname(os.path.realpath(__file__))

    allData = []
    points = []

    with open(DIRPATH+fileName) as f:
        for line in f:
            line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
            line = line.strip().split(',')
                
            allData.append(line)
    
    for crime in allData:
        if crime[19] != (""):
            if crime[19] != ("X_COORD_CD"):
               
                x = crime[19]
                y = crime[20]
                
                x = float(x)
                y = float(y)
                
                xprime = (x - minx) / deltax         # val (0,1)
                yprime = 1.0 - ((y - miny) / deltay) # val (0,1)
                
                xScreen = int(xprime*screenWidth)
                yScreen = int(yprime*screenHeight)

                points.append((xScreen,yScreen))
    
    return points

background_colour = (255,255,255)
manhattan_color = (194,35,38)
queens_color = (243,115,56)
staten_island_color = (253,182,50)
bronx_color = (2,120,120)
brooklyn_color = (129,22,56)

(width, height) = (1000, 1000)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('DBscan')
screen.fill(background_colour)

pygame.display.flip()

bronx_crimes = getPoints('\\NYPD_CrimeData\\filtered_crimes_bronx.csv', width, height)
brooklyn_crimes = getPoints('\\NYPD_CrimeData\\filtered_crimes_brooklyn.csv', width, height)
manhattan_crimes = getPoints('\\NYPD_CrimeData\\filtered_crimes_manhattan.csv', width, height)
queens_crimes = getPoints('\\NYPD_CrimeData\\filtered_crimes_queens.csv', width, height)
staten_island_crimes = getPoints('\\NYPD_CrimeData\\filtered_crimes_staten_island.csv', width, height)

running = True
while running:

    for p in bronx_crimes:
        pygame.draw.circle(screen, bronx_color, p, 1, 0)
    for p in brooklyn_crimes:
        pygame.draw.circle(screen, brooklyn_color, p, 1, 0)
    for p in manhattan_crimes:
        pygame.draw.circle(screen, manhattan_color, p, 1, 0)
    for p in queens_crimes:
        pygame.draw.circle(screen, queens_color, p, 1, 0)
    for p in staten_island_crimes:
        pygame.draw.circle(screen, staten_island_color, p, 1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    pygame.display.flip()