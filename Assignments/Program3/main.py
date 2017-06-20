"""
Program:
--------
    Program 3 - DBScan Earthquake Data

Description:
------------
    This program creates a json file with all earthquakes that have a magnitude of 7 and greater from 1960-2016
    It uses pygame to display each point represneting an earthquake with a visible color. 
    It adds a background image of the world to the output that is 1024x512
    
Name: Samuel Weems
Date: 22 June 2017
"""

import pygame
from get_quake_points import *
from display_quake_points import *
from adjust_quake_points import *
import sys,os

# Get current working path
DIRPATH = os.path.dirname(os.path.realpath(__file__))





#def get_earth_quake_data(year,month=[1,12],minmag=None,maxmag=None,query=True):




if __name__ == '__main__':

    years = []
    earthquake_points=[]


    for i in range(1960,2017):
        years.append(i) 
    
    get_earth_quake_data([years])

    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DBscan - Earthquake Data')


    bg = pygame.image.load(DIRPATH+'/background.png')


    pygame.display.flip()


    running = True
    while running:

        screen.blit(bg, (0, 0))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.flip()