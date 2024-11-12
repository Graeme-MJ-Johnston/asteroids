# dont forget source venv/bin/activate

import pygame
from circleshape import *
from player import *
from constants import *



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
       
        
        #draw player
        player.update(dt)
        player.draw(screen)
        
        
            
            #END OF GAME LOOP
        pygame.display.flip()
        dt = clock.tick(60) / 1000
            
            
            
 

if __name__ == "__main__":
    main()
    