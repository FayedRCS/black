# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame # type: ignore
from constants import *



def main():

    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clocka = pygame.time.Clock()
    dt = 0


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(000000)
        pygame.display.flip()
        
        dt = clocka.tick(60) / 1000



if __name__ == "__main__":
    main()

