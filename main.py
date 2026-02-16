import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
import player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets screen variable, using global constants in constants.py
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
        Player = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        Player.draw(screen)
        pygame.display.flip() # refresh?
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
