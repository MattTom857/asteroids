from constants import *
import pygame
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    #print("Hello from asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    i1 = 1;
    while (i1 == 1):
        log_state();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black");
        pygame.display.flip();            


if __name__ == "__main__":
    main()
