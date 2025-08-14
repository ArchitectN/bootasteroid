class Asteroids:
    def __init__(self, position, rotation):
        self.position = pygame.Vector2(position)
        self.rotation = rotation
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, (255, 255, 255), [(25, 0), (50, 50), (0, 50)])
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        # Update logic for the asteroid can be added here
        pass

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, new_rect.topleft)