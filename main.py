# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for group in updatable:
            group.update(dt)

        for asteroid in asteroids:
            if(player.is_colliding(asteroid)):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if(asteroid.is_colliding(shot)):
                    shot.kill()
                    asteroid.split()
        
        screen.fill("black")

        for group in drawable:
            group.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60)/1000





if __name__ == "__main__":
    main()