import pygame 

# Subclasses differ in:
# 1. Colour
# 2. Amount health

class Brick: 
    def __init__(self, xPos, yPos):
        self.width = 50
        self.height = 20
        self.xPos = xPos
        self.yPos = yPos
        self.health = 1
        self.colours = {
            1: (0, 225, 0)
        }
        self.is_destroyed = False
        self.score = 1

    def hit(self):
        self.health -= 1

        if self.health <= 0:
            self.is_destroyed = True

    def draw(self, screen):
        if not self.is_destroyed:
            pygame.draw.rect(screen, self.colours[self.health], (self.xPos, self.yPos, self.width, self.height))

class MegaBrick(Brick):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        
        # Override the health attribute
        self.health = 2

        self.colours = {
            1: (0, 225, 0),
            2: (255, 165, 0) # ---> rgba value
        }

        self.score = 3

class IndestructibleBrick(Brick):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        
        # Override the health attribute
        self.health = 3

        self.colours = {
            1: (0, 225, 0),
            2: (255, 165, 0),
            3: (255, 0, 0)
        }

        self.score = 5