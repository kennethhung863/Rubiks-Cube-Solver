import pygame

pygame.init()






class rectangle:
    def __init__(self, surface, color, x, y, length, width):
        self.surface = surface
        self.color = color
        self.x = x
        self.y = y
        self.length = length
        self.width = width
    #click = 0

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.length, self.width))

    # checks if the current rectangle is INSIDE the rectangle in parameter
    def intersects(self, rect1):
        x1 = rect1.x
        y1 = rect1.y
        length = rect1.length
        width = rect1.width
        
        if (self.x > x1 and self.x < (x1+length) and self.y > y1 and self.y < (y1+width)):
            return True
        else:
            return False
    
    def display_text(self, surface, color, x, y, size, str):

        font = pygame.font.SysFont('Calibri', size) 
        
        # create a text suface object, 
        # on which text is drawn on it. 
        text = font.render(str, True, color) 
        textRect = text.get_rect()  
        
        # set the center of the rectangular object. 
        textRect.center = (x, y) 
        surface.blit(text, textRect) 
