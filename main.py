import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Sets screen variable, using global constants in constants.py
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}") # Same as underneath
    print(f"Screen height: {SCREEN_HEIGHT}") # Don't think it's needed now, but leave it for now
    while 0 in range(0, 1): # infinite loop, game == running
        log_state() # runs the logger.py function log_state
        for event in pygame.event.get(): # calls event in pygame.event, likely an updating list of ongoing changes using user input
            if event.type == pygame.QUIT:
                return
            pass
        screen.fill("black") # Screen is object type pygame.display, so display type? .fill is a method, black is an argument
        pygame.display.flip() # refresh?
if __name__ == "__main__":
    main()
