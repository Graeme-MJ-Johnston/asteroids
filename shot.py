
import pygame
import constants
from circleshape import CircleShape




class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        rotation = 0
        
        
    def update(self, dt):
        self.position += self.velocity * dt
        
                 
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)