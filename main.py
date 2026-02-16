
import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets screen variable, using global constants in constants.py
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    asteroidfield.AsteroidField.containers = (updatable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (shots, updatable, drawable)

    AsteroidField = asteroidfield.AsteroidField()
    Player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}") # Same as underneath
    print(f"Screen height: {SCREEN_HEIGHT}") # Don't think it's needed now, but leave it for now
    while True: # infinite loop, game == running
        log_state() # runs the logger.py function log_state
        
        for event in pygame.event.get(): # calls event in pygame.event, likely an updating list of ongoing changes using user input
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black") # Screen is object type pygame.display, so display type? .fill is a method, black is an argument
        
        updatable.update(dt)
        for any in asteroids:
            if any.collides_with(Player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for any in asteroids:
            for bullet in shots:
                if any.collides_with(bullet):
                    log_event("asteroid_shot")
                    any.split()
                    bullet.kill()

        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip() # refresh?
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
