# it doesnt work . i hat e trig

class Bullet:
    def __init__(self, target, position):
        self.position = pygame.Vector2(position)
        self.target = pygame.Vector2(target)
        self.angle = self.position.angle_to(target)
        radians = math.atan2(target.x-position.y, target.x-position.x)
        angle = -math.degrees(radians)
        self.direction = pygame.Vector2(1, 0).rotate(angle)
        print(self.angle, self.direction, self.target)
    
    def tick(self):
        self.position += self.direction * 10
    
    def draw(self):
        pygame.draw.circle(screen, "#000000", self.position, 4)