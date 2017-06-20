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
import sys,os
import json

# Get current working path
DIRPATH = os.path.dirname(os.path.realpath(__file__))

if __name__ == '__main__':

  
    background_colour = (255,255,255)
    (width, height) = (1024, 512)
    color = (194,35,38)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('DBscan - Earthquake Data')
    bg = pygame.image.load(DIRPATH+'/background.png')
    pygame.display.flip()
   
    f = open('quake-assignment-adjusted.json','r')
    points = json.loads(f.read())
    
    running = True
    while running:

        screen.blit(bg, (0, 0))

        for p in points:
            pygame.draw.circle(screen, color, p, 1,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

  