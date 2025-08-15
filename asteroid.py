from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)


    def update(self, dt):
        # Update logic for the asteroid can be added here
        self.position += self.velocity * dt