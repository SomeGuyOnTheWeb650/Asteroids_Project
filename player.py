import circleshape
import constants
import pygame
import shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen,
                             "white",
                             self.triangle(),
                               constants.LINE_WIDTH)
    

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt


    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            
            self.shoot()

        self.shot_cooldown_timer -= dt
    
    
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        nose_position = self.position + forward * self.radius
        
        bullet = shot.Shot(nose_position.x, nose_position.y, constants.SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1)
        bullet.velocity = bullet.velocity.rotate(self.rotation)
        bullet.velocity = bullet.velocity * constants.PLAYER_SHOOT_SPEED
