import pygame
from circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
    
        super().__init__(self.x, self.y, radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    #def astroid_collision(self, target):
    #    return super().collide(target)
                 
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)