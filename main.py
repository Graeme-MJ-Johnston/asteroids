# dont forget source venv/bin/activate

# Imports
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
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
        pygame.display.flip()
        
        #draw player
        player.draw(screen)
        
            
            #END OF GAME LOOP
        dt = clock.tick(60) / 1000
            
            
            
 

if __name__ == "__main__":
    main()
    