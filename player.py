import circleshape
import constants
import pygame
import shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.is_respawning = False
        self.respawn_timer = 0
        self.lives = 3
        self.visible = True
        self.invincible_timer = 0
        self.is_invincible = False
        self.accel = 0

    
        
        
    
    def die(self):
        self.is_respawning = True
        self.respawn_timer = 3000
        self.visible = False
        



    
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
        if self.is_respawning:
            self.respawn_timer -= dt * 1000
            if self.respawn_timer <= 0:
                self.respawn()
            return
        if self.is_invincible:
            self.invincible_timer -= dt * 1000
            if self.invincible_timer <= 0:
                self.is_invincible = False
        
        
        self.inertia()
        self.accel -= dt / 3
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
            self.accel -= dt
        if keys[pygame.K_w]:
            self.move(dt)
            self.accel += dt
        if keys[pygame.K_SPACE]:
            
            self.shoot()

        self.shot_cooldown_timer -= dt
        
    
    
    def inertia(self):
        inertia = pygame.Vector2(0, 1).rotate(self.rotation) * self.accel
        self.position += inertia






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


    def respawn(self):
        
        self.is_respawning = False
        self.visible = True
        self.position = pygame.Vector2(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
        self.is_invincible = True
        self.invincible_timer = 3000


    