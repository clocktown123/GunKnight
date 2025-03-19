import pygame
import math
import random
from bullet_types import Bullet

bullets = []

def shoot(bullet_type, target, position):
    bullet = bullet_type(target, position) # bullet_type should be a class
    global bullets
    bullets.append(bullet)

print(__name__)

if __name__ == "__main__": # prevents an error
    from Enemy import Slime, Skeleton

    screen = pygame.display.set_mode((640, 360))

    pygame.init()

    player_pos = pygame.Vector2(0, 0)
    player_size = pygame.Vector2(32, 32)
    mouse_pos = pygame.Vector2(0, 0)
    player_speed = 5

    running = True
    clock = pygame.time.Clock()

    slime = Slime((600, 200), "#00FF00", (32, 32), 50)
    skeleton = Skeleton((610, 310), "#808080", (20, 20), 20)
    ticker = 0

    Level = 1

    # Skeleton = Skeleton((400, 300), (211,211,211), (50, 50))

    def get_axis(negative, positive):
        return pygame.key.get_pressed()[positive] - pygame.key.get_pressed()[negative]

    pygame.mixer.music.load("bgm.mp3") # we need doom eternal ost "all they have to fear is you" to survive
    pygame.mixer.music.play(loops=-1)

    sounds_to_load = [
        "fire.wav"
    ]

    enemies = [
        skeleton
    ]

    sounds = []

    for i in sounds_to_load:
        sounds.append(pygame.mixer.Sound(i))
        print(f"loaded {i}")

    def play_sound(min_id, max_id):
        sid = random.randint(min_id, max_id)
        sounds[sid].play()

    while running:
        ticker += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEMOTION: mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN: shoot(Bullet, mouse_pos, player_pos + (player_size / 2)); play_sound(0, 0)
        
        player_pos.x += get_axis(pygame.K_a, pygame.K_d) * player_speed
        player_pos.y += get_axis(pygame.K_w, pygame.K_s) * player_speed

        #for i in bullets: i.draw(screen); i.tick()

        bfr = enemies.copy()

        for i in enemies:
            i.tick(player_pos, ticker)

            if i.collide_all(bullets): i.hp -= 10; print(i)
            if not i.isAlive: bfr.remove(i)
        
        enemies = bfr.copy()
        
        screen.fill("#FFFFFF")

        for i in bullets:
            i.draw(screen)
            i.tick()
        
        for i in enemies:
            i.draw(screen)

        pygame.draw.rect(screen, (21,21,21), (player_pos, player_size))
        pygame.draw.rect(screen, (225,225,225), (player_pos, (10, 10)))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

#♒︎□︎□︎♌︎◆︎⬧︎ ♑︎●︎□︎□︎♌︎◆︎⬧︎
# if you want to test: copy/paste all the code into a local vscode (another window)
# ctrl a -> ctrl c -> move windows -> ctrl a -> ctrl v