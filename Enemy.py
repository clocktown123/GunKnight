import pygame
import random
from utils import *

# setup_extra_vars() -> use to uh, setup extra self-scope variables
# tick(self, target) -> ran every game tick, target should be whatever position it's targeting
# draw(self, screen) -> renders the enemy

class Enemy:
    def setup_extra_vars(self): # define this per class
        return

    def __init__(self, position, color, size):
        self.position = pygame.Vector2(position)
        self.size = pygame.Vector2(size)
        self.color = color

        self.setup_extra_vars()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size))

    def tick(self, target):
        raise NotImplementedError("needs to be overridden by subclass")

class Slime(Enemy):
    def setup_extra_vars(self):
        self.speed = 5

    def tick(self, target):
        dt = dir_to(target, self.position) * self.speed
        # print(dt)
        self.position += dt

class Skeleton(Enemy):
    def __init__ (self, x, y,)
    def tick(self, target):
      
        
# rewrote this (-liam)

# class Slime:
#     def __init__(self, x, y, color, width, height,ticker,RIGHT,LEFT,DOWN,UP):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.width = width
#         self.height = height
#         self.ticker= ticker
#         self.LEFT = LEFT
#         self.RIGHT = RIGHT
#         self.DOWN = DOWN
#         self.Up = UP


#     def draw(self, screen):
#         pygame.draw.rect(screen, (102,255,102), (self.x, self.y, self.width, self.height))

#     def move(self,ticker,RIGHT,LEFT,DOWN,UP):
#         if ticker % 40 == 0:
#             num = random.randrange(0,4)
#             if num ==0:
#                 self.direction = RIGHT
#             elif num == 1:
#                 self.direction = LEFT
#             if num ==2:
#                 self.direction = DOWN
#             elif num == 3:
#                 self.direction = UP
       
            