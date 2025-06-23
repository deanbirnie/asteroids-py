import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    
    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while (1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        # Instantiate a player object
        player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
        player.draw(screen)

        pygame.display.flip()
        
        # limit FPS to 60 and decouple game from CPU cycles
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
