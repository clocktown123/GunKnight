import pygame
import random
from utils import dir_to

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
    def setup_extra_vars(self):
        self.speed = 0
    def tick(self, target):
        dt = dir_to(target, self.position) * self.speed
        # print(dt)
        self.position += dt
    # def shootCD(self, ticker, shoot, Bullet, playerPos):
    #     shoot(Bullet, playerPos, self.position + (self.size / 2))


        
# rewrote this (-liam)
       
            