import math
import pygame



# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collide(self, threat):
        #Find the distance
        distance = pygame.math.Vector2.distance_to(self.position, threat.position)
        
        #check for collision
        if distance > self.radius + threat.radius:
            return False
        else:
            return True
        

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass