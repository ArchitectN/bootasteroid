from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)


    def update(self, dt):
        # Update logic for the asteroid can be added here
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # Create two smaller asteroids
            angle = random.uniform(20, 50)
            first_velocity = self.velocity.rotate(angle) * 1.2
            second_velocity = self.velocity.rotate(-angle) * 1.2

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            first_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            first_asteroid.velocity = first_velocity
            first_asteroid.add(self.containers)
            second_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            second_asteroid.velocity = second_velocity
            second_asteroid.add(self.containers)