import circleshape, constants, pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__( x, y, SHOT_RADIUS)
        


    def draw(self, screen):
        center = (self.position.x, self.position.y)
        color ="white"
        width = 2
        surface = screen
        pygame.draw.circle(surface, color, center, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)