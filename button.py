import pygame
from rectangle import rectangle
pygame.init()






class button(rectangle):
    def __init__(self, surface, color, x, y, length, width, text, text_color, text_size):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.width))
        self.display_text(self.surface, self.text_color, self.x + self.length/2, self.y + self.width/2, self.text_size, self.text)
        


