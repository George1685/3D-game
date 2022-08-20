import pygame as pg
from random import *
from time import sleep

pg.init()

pg.display.set_mode((255, 255))
pg.display.set_caption("3D Test","Cube")
surface = pg.Surface((255, 255))

pg.display.flip()

screen = pg.display.get_surface()

cursor, mask = pg.cursors.compile(['        ','        ','        ','        ','    o   ','        ','        ','        '], "X", ".", "o")
hotspot = 4,4
size = 8,8
pg.mouse.set_cursor(size, hotspot, cursor, mask)

def show(image):
    global screen         
    screen.blit(image, (0, 0))
    pg.display.flip()
    pg.event.pump()
 

def disp(pixels):
    global surface
    ar = pg.PixelArray(surface)
    for x,y,color in pixels:          
        ar[x,y] = color
    del ar
    show(surface)



