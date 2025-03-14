# it doesnt work . i hat e trig
import pygame
import math

class Bullet:
    def __init__(self, target, position):
        self.position = pygame.Vector2(position)
        self.target = pygame.Vector2(target)
        self.direction = pygame.Vector2(self.target.x - self.position.x, self.target.y - self.position.y) # stolen from godot: https://github.com/godotengine/godot/blob/87f897ae0ad5a6770c6ee267e2f3458c89a06df7/core/math/vector2.h#L302
        self.direction.normalize_ip()
    
    def tick(self):
        self.position += self.direction * 10
    
    def draw(self, screen):
        pygame.draw.circle(screen, "#808080", self.position, 4)