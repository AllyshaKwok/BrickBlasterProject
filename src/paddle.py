import pygame 

class Paddle: 
    def __init__(self, screen_width, screen_height):
        self.width = 100
        self.height = 10
        self.xPos = (screen_width - self.width) // 2
        self.yPos = screen_height - 50
        self.speed = 8
        self.screen_width = screen_width

    def move_left(self):
        self.xPos = max(0, self.xPos - self.speed) 

    def move_right(self):
        self.xPos = min(self.screen_width - self.width, self.xPos + self.speed)

    def draw(self, screen):
        pygame.draw.rect(screen, (225, 225, 225), (self.xPos, self.yPos, self.width, self.height))