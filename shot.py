import pygame
from circleshape import CircleShape
from constants import *



class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        # Update logic for the asteroid can be added here
        self.position += self.velocity * dt