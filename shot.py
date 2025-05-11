import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def update(self, dt):
        base = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += base * PLAYER_SHOOT_SPEED * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
