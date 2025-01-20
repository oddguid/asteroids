import pygame
import random
from circleshape import CircleShape
from constants import *

# class for asteroid
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def move(self, dt):
        self.position += (self.velocity * dt)

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            # small asteroid
            return

        # generate random angle
        random_angle = random.uniform(20, 50)

        # directions for new asteroids
        direction_one = self.velocity.rotate(random_angle)
        direction_two = self.velocity.rotate(-random_angle)

        # radius for new asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create asteroids
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = direction_one * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = direction_two * 1.2

