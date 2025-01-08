
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.copy().rotate(random_angle)
        vector_two = self.velocity.copy().rotate(-random_angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one = Asteroid(self.position.x, self.position.y, child_radius)
        child_two = Asteroid(self.position.x, self.position.y, child_radius)
        speed_increase = 1.2
        child_one.velocity = vector_one * speed_increase
        child_two.velocity = vector_two * speed_increase

