import pygame
from constants import *


def main():
    pygame.init()
    
    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while (1):
        screen.fill("#000000")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        ms = game_clock.tick(60)
        dt = ms / 1000


if __name__ == "__main__":
    main()
