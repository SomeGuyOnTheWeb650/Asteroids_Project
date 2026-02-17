import circleshape
import constants
import pygame
from logger import *
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)



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

