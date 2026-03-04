from constants import PLAYER_RADIUS, LINE_WIDTH
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED;
from circleshape import CircleShape;
import pygame;

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH);

    def update(self,dt):
        self.position = self.position + self.velocity * dt;
