import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    containers = ()

    def __init__(self, x, y, radius,velocity):
        super().__init__(x,y,radius)
        self.velocity = velocity

        for group in self.containers:
            group.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position  

        self.kill() 

        if self.radius <= ASTEROID_MIN_RADIUS:
            return   

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        Asteroid(self.position.x, self.position.y, new_radius, velocity1)
        Asteroid(self.position.x, self.position.y, new_radius, velocity2)
