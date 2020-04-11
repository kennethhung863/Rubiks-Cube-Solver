import pygame
from rectangle import rectangle

pygame.init()
# color variables for increment
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
orange = ((255,150,0))
yellow = ((255,255,0))
colors = [blue, red, green, orange, yellow, white]






class square(rectangle):
    def __init__(self, surface, color, x, y, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = width
        self.width = width
    


    def color_increment(self):
        for i in range(0,6):
            if self.color == colors[i]:
                if i==5:
                    self.color = colors[0]
                else:
                    self.color = colors[i+1]
                break