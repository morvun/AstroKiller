import pygame
from constants import *
from player import Player

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = updateable, drawable

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt = float(0)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))

        for updates in updateable:
            updates.update(dt)

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()
        dt = fps.tick(FPS) / 1000.0  # Delta time in seconds

    
#    print("Starting Asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
