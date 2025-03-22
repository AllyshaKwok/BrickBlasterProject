import pygame 

class Brick: 
    def __init__(self, xPos, yPos):
        self.width = 50
        self.height = 20
        self.xPos = xPos
        self.yPos = yPos
        self.speed = 5
        self.is_destroyed = False

    def draw(self, screen):
        if not self.is_destroyed:
            pygame.draw.rect(screen, (0, 225, 0), (self.xPos, self.yPos, self.width, self.height))