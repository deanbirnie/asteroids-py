import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_ang = random.uniform(20, 50)
        vector1 = self.velocity.rotate(rand_ang)
        vector2 = self.velocity.rotate(-rand_ang)
        
        rad1 = self.radius - ASTEROID_MIN_RADIUS
        rad2 = self.radius - ASTEROID_MIN_RADIUS

        new1 = Asteroid(self.position.x, self.position.y, rad1)
        new2 = Asteroid(self.position.x, self.position.y, rad2)

        new1.velocity = vector1 * 1.2
        new2.velocity = vector2 * 1.2
