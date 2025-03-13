import pygame
import random
class enemy:
    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def update(self, delta_time):
        raise NotImplementedError("needs to be overridden by subclass")
    
class slime:
    def __init__(self, x, y, color, width, height,ticker,RIGHT,LEFT,DOWN,UP):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.ticker= ticker
        self.LEFT = LEFT
        self.RIGHT = RIGHT
        self.DOWN = DOWN
        self.Up = UP


    def draw(self, screen):
        pygame.draw.rect(screen, (102,255,102), (self.x, self.y, self.width, self.height))

    def move(self,ticker,RIGHT,LEFT,DOWN,UP):
        if ticker % 40 == 0:
            num = random.randrange(0,4)
            if num ==0:
                self.direction = RIGHT
            elif num == 1:
                self.direction = LEFT
            if num ==2:
                self.direction = DOWN
            elif num == 3:
                self.direction = UP
       
            