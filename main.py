import pygame
import math
from bullet_types import Bullet
from Enemy import Slime, Skeleton
#♒︎□︎□︎♌︎◆︎⬧︎ ♑︎●︎□︎□︎♌︎◆︎⬧︎
#i like apples and bananas
#me too man, me too
# nobody cares !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#i care ;-;
#hiiiiii i love jay<3
# if you want to test: copy/paste all the code into a local vscode (another window)
# ctrl a -> ctrl c -> move windows -> ctrl a -> ctrl v

screen = pygame.display.set_mode((640, 360))

player_pos = pygame.Vector2(0, 0)
player_size = pygame.Vector2(32, 32)
mouse_pos = pygame.Vector2(0, 0)
player_speed = 5

running = True
clock = pygame.time.Clock()

slime = Slime((600, 200), "#00FF00", (32, 32))
skeleton = Skeleton((610, 310), "#808080", (20, 20))

ticker = 0

# Skeleton = Skeleton((400, 300), (211,211,211), (50, 50))

bullets = []

def shoot(bullet_type, target, position):
    bullet = bullet_type(target, position) # bullet_type should be a class
    print(bullet)
    global bullets
    bullets.append(bullet)

def get_axis(negative, positive):
    return pygame.key.get_pressed()[positive] - pygame.key.get_pressed()[negative]

while running:
    ticker += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEMOTION: mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN: shoot(Bullet, mouse_pos, player_pos + (player_size / 2))
    
    player_pos.x += get_axis(pygame.K_a, pygame.K_d) * player_speed
    player_pos.y += get_axis(pygame.K_w, pygame.K_s) * player_speed

    if ticker > 50:
        ticker = 0
        shoot(Bullet, player_pos, skeleton.position + (skeleton.size / 2))

    #for i in bullets: i.draw(screen); i.tick()
    
    screen.fill("#FFFFFF")

    for i in bullets:
        i.draw(screen)
        i.tick()
    
    slime.tick(player_pos)
    slime.draw(screen)

    skeleton.draw(screen)

    pygame.draw.rect(screen, (21,21,21), (player_pos, player_size))

    pygame.display.update()

    clock.tick(60)

pygame.quit()