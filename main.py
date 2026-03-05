from logger import log_state, log_event
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys

def main():
    #print("Hello from asteroids!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock();
    dt = 0;

    updatable = pygame.sprite.Group();
    drawable = pygame.sprite.Group();
    asteroids = pygame.sprite.Group();
    shots = pygame.sprite.Group();
    Player.containers = (updatable,drawable);
    Asteroid.containers = (updatable,drawable,asteroids);
    AsteroidField.containers = (updatable);
    Shot.containers = (updatable,drawable,shots)
    
    ship = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2);
    rocks = AsteroidField();

    i1 = 1;
    while (i1 == 1):
        log_state();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black");
        for object in updatable:
            object.update(dt);
        for object in drawable:
            object.draw(screen);
        for object in asteroids:
            if ship.collides_with(object):
                log_event("player_hit");
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(object):
                    log_event("asteroid_shot");
                    object.split();
                    bullet.kill();
        pygame.display.flip();
        dt = clock.tick(60) / 1000;
        print(dt);

if __name__ == "__main__":
    main()
