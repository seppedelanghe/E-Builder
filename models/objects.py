from models.vector import Vector
from models.particle import Particle
from services.statics import BLACK

import pygame

class Triangle(Particle):
    def __init__(self,
                tip: Vector,
                width: int,
                speed: float,
                direction: float,
                angle: float = 0,
                mass:float = 0,
                gravity:float = 0,
                bounce:float = 0,
                friction:float = 0,
                color: tuple = BLACK):

        
        super().__init__(tip.x, tip.y, speed, direction, mass, gravity, bounce, friction)
        self.color = color
        self.tip = tip
        self.width = width
        self.angle = angle

    def draw(self, screen):
        leg1 = Vector(self.width, -(self.width / 2))
        leg2 = Vector(self.width, self.width / 2)

        leg1.setAngle(self.angle - (1 / 3) * 180)
        leg2.setAngle(self.angle + (1 / 3) * 180)
        
        pygame.draw.lines(screen, BLACK, True, [
            self.coordinates,
            self.position.v_add(leg1).coordinates,
            self.position.v_add(leg2).coordinates,
        ])

class Circle(Particle):
    def __init__(self,
                x, y,
                radius, 
                speed: float,
                direction: float,
                mass:float = 0,
                gravity:float = 0,
                bounce:float = 0,
                friction:float = 0,
                color: tuple = BLACK):

        super().__init__(x, y, speed, direction, mass, gravity, bounce, friction)
        self.radius = radius
        self.color = color

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def collisionCircle(self, c1):
        return self.distanceTo(c1) <= self.radius + c1.radius

    def collisionParticle(self, p1):
        return self.distanceTo(p1) < self.radius

class Rect(Particle):
    def __init__(self,
                x1: float, y1:float,
                x2: float, y2: float, 
                speed: float,
                direction: float,
                mass:float = 0,
                gravity:float = 0,
                bounce:float = 0,
                friction:float = 0,
                color: tuple = BLACK):

        x = x2 - x1
        y = y2 - y1
        super().__init__(x, y, speed, direction, mass, gravity, bounce, friction)

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
        self.color = color

    @property
    def width(self):
        return self.x2 - self.x1

    @property
    def height(self):
        return self.y2 - self.y1

    @property
    def coordinates(self):
        return (self.x1, self.y1, self.x2, self.y2)

    @property
    def center(self):
        return (self.position.x, self.position._y)

    def collisionCircle(self, c1):
        cx = c1.position.x
        cy = c1.position._y
        
        if cx + c1.radius >= self.x1 and cx - c1.radius <= self.x2:
            if cy + c1.radius >= self.y1 and cy - c1.radius <= self.y2:
                return True
        return False

    def collisionParticle(self, p1):
        px = p1.position.x
        py = p1.position._y
        
        if px >= self.x1 and px <= self.x2:
            if py >= self.y1 and py <= self.y2:
                return True
        return False