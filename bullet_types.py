# it doesnt work . i hat e trig
import pygame
from utils import dir_to

class Bullet:
    def __init__(self, target, position):
        self.position = pygame.Vector2(position)
        self.target = pygame.Vector2(target)
        self.direction = dir_to(target, position)
    
    def tick(self):
        self.position += self.direction * 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#808080", self.position, 4)