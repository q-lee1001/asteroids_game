import circleshape, constants, pygame, random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        


    def draw(self, screen,):
        center = (self.position.x, self.position.y)
        color ="white"
        width = 2
        surface = screen
        pygame.draw.circle(surface, color, center, self.radius, width)

    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            neg_vec = self.velocity.rotate(-angle)
            pos_vec = self.velocity.rotate(angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ast_a = Asteroid(self.position.x, self.position.y, new_rad)
            ast_b = Asteroid(self.position.x, self.position.y, new_rad)
            ast_a.velocity = neg_vec * 1.2
            ast_b.velocity = pos_vec * 1.2
