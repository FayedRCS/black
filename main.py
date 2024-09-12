import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    updatable.add(player)
    drawable.add(player)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #updates
        for i in updatable:
            i.update(dt)

        #rendering

        screen.fill("black")
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS / controling framerate
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
