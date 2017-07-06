"""
Program:
--------
    Program 6 - heat_map.py

Description:
------------
   This program generates a heat style map showing terrorist hotspots around the world based on city coordinates.


Name: Samuel Weems
Date: 07 July 2017
"""

import json
import os,sys
import pygame
import random 
import math
import pprint as pp



EPSILON = sys.float_info.epsilon  # smallest possible difference
  
screen_width = 1024
screen_height = 512

def convert_to_rgb(minval, maxval, val, colors):
    fi = float(val-minval) / float(maxval-minval) * (len(colors)-1)
    i = int(fi)
    f = fi - i
    if f < EPSILON:
        return colors[i]
    else:
        (r1, g1, b1), (r2, g2, b2) = colors[i], colors[i+1]
        return int(r1 + f*(r2-r1)), int(g1 + f*(g2-g1)), int(b1 + f*(b2-b1))

def mercX(lon,zoom = 1):
    lon = math.radians(lon)
    a = (256 / math.pi) * pow(2, zoom)
    b = lon + math.pi
    return a * b

def mercY(lat,zoom = 1):
    lat = math.radians(lat)
    a = (256.0 / math.pi) * pow(2, zoom)
    b = math.tan(math.pi / 4 + lat / 2)
    c = math.pi - math.log(b)
    return (a * c)

def adjust_point(p):
       
        voffset = 0
        hoffset = 0

        lon,lat = p
        x = (mercX(lon) / 1024 * screen_width) - hoffset
        scale = 1 / math.cos(math.radians(lat))             # not used
        y = (mercY(lat) / 512 * screen_height) - (screen_height/2) - voffset
        return (x,y)

if __name__ == '__main__':

# Load terrorism data

    with open('attacks.json', 'r') as content_file:
        content = content_file.read()
    terrorism_dict = json.loads(content)

# Gather Data for display and calculation
    city_totals = []
    city_coordinates = []
    adjusted_city_coordinates= []
    

    for k,v in terrorism_dict.items():
        for k2,v2 in v.items():
            city_totals.append(v2['count'])
            city_coordinates.append(v2['geometry']['coordinates'])
    
  
    for p in city_coordinates:
        adjusted_city_coordinates.append(adjust_point(p))



# Calculate color mapping values

    range_values = []
    color = []
    steps = 25

    maxval = max(city_totals)
    minval = min(city_totals)
   
    delta = float(maxval-minval) / steps
    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]  # [BLUE, GREEN, RED]
 
    for i in range(steps+1):
        val = minval + i*delta
        r, g, b = convert_to_rgb(minval, maxval, val, colors)
        range_values.append(val)
        color.append((r,g,b))
    
    range_values.append(maxval+1)
    city_color_key = []
    radius_range = []
    radius_key = []

    for i in range (len(range_values)):
        radius_range.append(i+1)
   
    for i in range (len(adjusted_city_coordinates)):
        for j in range (len(range_values)-1):
            if city_totals[i] >= range_values[j] and city_totals[i] < range_values[j+1]:     
                city_color_key.append(color[j])
                radius_key.append(radius_range[j])
    
    

   
    

# Display

    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Terrorism Heat Map by City')
    bg = pygame.image.load ('background.png')
    pygame.display.flip()

    running = True
    while running:

        screen.blit(bg, (0, 0))

        for i in range (len(adjusted_city_coordinates)):
            x,y = adjusted_city_coordinates[i]
            pygame.draw.circle(screen, city_color_key[i], (int(x), int(y)), radius_key[i],int(radius_key[i]))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

#pygame.draw.circle(Surface, color, pos, radius, width=0)



 



# mf.run()










