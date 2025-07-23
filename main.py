# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants, player 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    
    player1 = player.Player(x = constants.SCREEN_WIDTH / 2, y = constants.SCREEN_HEIGHT / 2 )
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        
        player1.draw(screen)
        
        pygame.display.flip()
        
        # Pause the game loop until 1/60th of a second has passed.
        clock.tick(60)
        dt = clock.tick() / 1000

        
if __name__ == "__main__":
    main()
