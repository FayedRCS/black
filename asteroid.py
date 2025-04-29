from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen, radius):
        pygame.draw.circle(screen, radius, width = 2)

 #Breaktime