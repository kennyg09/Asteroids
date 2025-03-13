import pygame
from constants import *  
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game Over")
                pygame.quit()
                return

        for asteroid in asteroids:
            for shot in shots:
                if shot.check_collision(asteroid):  
                    shot.kill()  
                    asteroid.split()

        screen.fill(BLACK)
        for obj in drawable:
            obj.draw(screen)

      

        pygame.display.flip()
       
    pygame.quit()

if __name__ == "__main__":
    main()
