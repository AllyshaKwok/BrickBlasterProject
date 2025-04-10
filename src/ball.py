import pygame 
import random

class Ball: 
    def __init__(self, screen_width, screen_height):
        self.radius = 8
        self.xPos = (screen_width - self.radius) // 2
        self.yPos = (screen_height - self.radius) // 2
        self.speed_x = random.randint(3, 8) * random.choice([-1, 1])
        self.speed_y = random.randint(3, 8)
        self.screen_width = screen_width
        self.screen_height = screen_height
    
    def move(self):
        self.xPos += self.speed_x
        self.yPos += self.speed_y

        # Checks if it hits the left wall or right wall
        if self.xPos <= 0 or self.xPos >= self.screen_width:
            self.speed_x *= -1
        
        if self.yPos <= 0:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.xPos, self.yPos), self.radius)