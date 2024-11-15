import pygame
import random
from circleshape import CircleShape
from constants import *



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
    
        super().__init__(x, y, radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
                 
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            
            asteroid_a_vec = pygame.math.Vector2.rotate(self.velocity, angle)
            asteroid_b_vec = pygame.math.Vector2.rotate(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            

            asteroid_a.velocity = asteroid_a_vec * 1.2
            asteroid_b.velocity = asteroid_b_vec * 1.2