#!/home/novicegentry/workspace/JAMES/asteroids_pygame_project/.venv/bin/python3
import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
import player
import asteroid
import asteroidfield
import shot
import random


def clear_spawn_zone(asteroids, center, radius=100):
        for asteroid in asteroids:
            distance = (asteroid.position.distance_to(center))
            if distance < radius:
                asteroid.kill()







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
    asteroidfield.ScoreCounter.containers = (drawable, updatable)



    
    counter = asteroidfield.ScoreCounter()
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
        if Player.visible == False:
            clear_spawn_zone(asteroids, pygame.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        for any in asteroids:
            if Player.is_invincible:
                break
            elif any.collides_with(Player):
                if Player.visible:
                    log_event("player_hit")
                    Player.die()
                    Player.lives -= 1
                    if Player.lives == 0: 
                        print("Game over!")
                        print(f"Final Score: {counter.score}")
                        sys.exit()
                
                
                

        
        for any in asteroids:
            for bullet in shots:
                if any.collides_with(bullet):
                    log_event("asteroid_shot")
                    any.split()
                    bullet.kill()
                    counter.score += 10

        for a in asteroids:
            new_asteroids = asteroids.copy()
            new_asteroids.remove(a)
            for new in new_asteroids:
                
                
                if a.collides_with(new):
                    
                    if a.time_since_collision >= 1 and new.time_since_collision >= 1:
                        
                        direction = new.position - a.position
                        if direction.length() > 0:
                            direction = direction.normalize()

                        speed_a = a.velocity.length()
                        speed_new = new.velocity.length()

                        a.velocity = (-direction * speed_a).rotate(random.randint(-10, 10))
                        new.velocity = (direction * speed_new).rotate(random.randint(-10, 10))
                        
                        

                        a.time_since_collision = 0
                        new.time_since_collision = 0    
                    


        for sprite in drawable:
            if hasattr(sprite, "visible"):
                if sprite.visible == False:
                    continue
                elif sprite.visible:
                    sprite.draw(screen)
            
            else:
                sprite.draw(screen)
        pygame.display.flip() # refresh?
        
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
