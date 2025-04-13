import pygame 
import random

class Ball: 
    def __init__(self, screen_width, screen_height):
        self.radius = 8
        self.xPos = (screen_width - self.radius) // 2
        self.yPos = (screen_height - self.radius) // 2
        self.speed_x = 0
        self.speed_y = random.randint(5, 7)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.colour = (255, 0, 0)
        self.damage = 1
    
    def move(self):
        self.xPos += self.speed_x
        self.yPos += self.speed_y

        # Checks if it hits the left wall or right wall
        if self.xPos <= 0 or self.xPos >= self.screen_width:
            self.speed_x *= -1
        
        if self.yPos <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (self.xPos, self.yPos), self.radius)

class BigBall(Ball):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)

        self.radius = 16
        self.colour = (0, 255, 0)
        self.speed_y = 4

class StrongBall(Ball):
    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)

        self.damage = 3
        self.colour = (255, 255, 0)