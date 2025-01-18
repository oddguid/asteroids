import pygame
import sys
from constants import *
from player import Player

def main() -> int:
    print("Starting asteroids!")

    # Initialize pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # clock for framerate
    clock = pygame.time.Clock()
    dt = 0

    # player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update player
        player.update(dt)

        # render
        screen.fill((0, 0, 0))

        player.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == '__main__':
    sys.exit(main())

