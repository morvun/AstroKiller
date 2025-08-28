import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroidfield import *
from shot import Shot

updateables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
astroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = updateables, drawables
Asteroid.containers = updateables, drawables, astroids
AsteroidField.containers = updateables
Shot.containers = updateables, drawables, shots

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = float(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))

        for update in updateables:
            update.update(dt)
        
        for asteroid in astroids:
            if player.check_collision(asteroid):
                print("Game Over!")
                pygame.quit()
                return
            
        for asteroid in astroids:
            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
                    break

        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in astroids:
            asteroid.draw(screen)

        pygame.display.flip()
        dt = fps.tick(FPS) / 1000.0  # Delta time in seconds

    
#    print("Starting Asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
