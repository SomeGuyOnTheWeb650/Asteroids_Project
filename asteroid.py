import circleshape
import constants
import pygame
from logger import *
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.time_since_collision = 0


    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            constants.LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt
        self.time_since_collision += dt
        if self.position.x > constants.SCREEN_WIDTH:
            self.position.x = self.position.x - constants.SCREEN_WIDTH - (self.radius * 2)
        if self.position.x < 0:
            self.position.x = self.position.x + constants.SCREEN_WIDTH + (self.radius * 2)
        if self.position.y > constants.SCREEN_WIDTH:
            self.position.y = self.position.y - constants.SCREEN_HEIGHT - (self.radius * 2)
        if self.position.y < 0:
            self.position.y = self.position.y - constants.SCREEN_HEIGHT + (self.radius * 2)        

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
                
            
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        ast1_vector = self.velocity.rotate(angle)
        ast2_vector = self.velocity.rotate(-angle)
        ast_new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, ast_new_radius)
        ast1.velocity = ast1_vector * 1.2
        ast2 = Asteroid(self.position.x, self.position.y, ast_new_radius)
        ast2.velocity = ast2_vector * 1.2

