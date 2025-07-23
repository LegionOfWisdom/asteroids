# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants as c

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {c.SCREEN_WIDTH}\nScreen height: {c.SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color="black")
        pygame.display.flip()
    

    
if __name__ == "__main__":
    main()
