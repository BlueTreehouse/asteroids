import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    clock = pygame.time.Clock()
    dt = 0
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    #initialization code
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    #game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        
        for object in drawable:
            object.draw(screen)
        
        updatable.update(dt)
        

        for ast in asteroids:
            if player.collision(ast):
                print("Game Over!")
                sys.exit()

        
            for bullet in shots:
                if bullet.collision(ast):
                    bullet.kill()
                    ast.split()


        pygame.display.flip()
        
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()