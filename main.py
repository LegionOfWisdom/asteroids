import sys
import pygame # type: ignore
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Initialization Code
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    
    player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2 )
    asteroidField = AsteroidField()
    
    dt = 0
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collions(player1):
                return sys.exit("Game over!")
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collions(asteroid):
                    shot.kill()
                    asteroid.split()
                    
        screen.fill(color="black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()
        
        # Pause the game loop until 1/60th of a second has passed.
        dt = clock.tick(60) / 1000

        
if __name__ == "__main__":
    main()
