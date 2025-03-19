import pygame
import random
from utils import dir_to
from bullet_types import Bullet

from main import shoot

# setup_extra_vars() -> use to uh, setup extra self-scope variables
# tick(self, target) -> ran every game tick, target should be whatever position it's targeting
# draw(self, screen) -> renders the enemy

class Enemy:
    def setup_extra_vars(self): # define this per class
        return

    def __init__(self, position, color, size, hp):
        self.position = pygame.Vector2(position)
        self.size = pygame.Vector2(size)
        self.color = color
        self.hitbox = pygame.Rect(self.position, self.size)
        self.hp = hp
        self.isAlive = True

        self.setup_extra_vars()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position, self.size))

    def tick(self, target, ticks = 0):
        raise NotImplementedError("needs to be overridden by subclass")
    
    def collision(self, bulletPos):
        return self.hitbox.collidepoint(bulletPos)
    
    def collide_all(self, bullets):
        for i in bullets:
            if self.hitbox.collidepoint(i.position):
                bullets.remove(i)
                return True
        
        return False

    def LifeCheck(self):
        if self.hp <= 0:
            self.isAlive = False
        else:
            self.isAlive = True
                                                                                                                                        #ik and ive been crying alot these past few days and i mean alot and no i know ur super busy and i dont want to put u thoug more ik ur classes are even harder then mine 
class Slime(Enemy):
    def setup_extra_vars(self):
        self.speed = 5

    def tick(self, target):
        dt = dir_to(target, self.position) * self.speed
        # print(dt)
        self.position += dt

class Skeleton(Enemy):
    def setup_extra_vars(self): # still need this lol
        self.speed = 0

    #def setup_extra_vars(self):
    def tick(self, target, ticks):

        if ticks % 50 == 0:
            print("should shoot")
            shoot(Bullet, target, self.position + (self.size / 2))
    

        
    # def shootCD(self, ticker, shoot, Bullet, playerPos):
    #     shoot(Bullet, playerPos, self.position + (self.size / 2))


        
# rewrote this (-liam)
       
            