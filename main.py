# dont forget source venv/bin/activate

import pygame
from circleshape import CircleShape
from player import *
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():
    pygame.init
    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #timing settings
    clock = pygame.time.Clock()
    dt = 0
    
    #Player creation
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroidfield = AsteroidField()
    
    
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    
    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(('black'))
       
        
        #update positions
        for updates in updatable:
            updates.update(dt)
            
        #Checking for collisions
        for roid in asteroids:
            if player.collide(roid):
                print("Game over!")
                sys.exit()
            
        
        #draw objects
        for draws in drawable:
            draws.draw(screen)
        
        
        
        
        
            
            #END OF GAME LOOP
        pygame.display.flip()
        dt = clock.tick(60) / 1000
            
            
            
 

if __name__ == "__main__":
    main()
    