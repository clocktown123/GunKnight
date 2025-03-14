import pygame

def dir_to(t, p):
    target = pygame.Vector2(t)
    position = pygame.Vector2(p)
    d = pygame.Vector2(target.x - position.x, target.y - position.y) # stolen from godot: https://github.com/godotengine/godot/blob/87f897ae0ad5a6770c6ee267e2f3458c89a06df7/core/math/vector2.h#L302
    if d.length() == 0: return d
    return d.normalize()