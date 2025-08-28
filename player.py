from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
import pygame

# Player class inheriting from CircleShape
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0  # in degrees
        self.timer = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                shot = self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
                return shot

    def shoot(self):
        tip = self.triangle()[0]  # Tip of the ship
        Shot_instance = Shot(tip.x, tip.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        Shot_instance.velocity = forward * PLAYER_SHOT_SPEED  # Set shot speed
        return Shot_instance
    