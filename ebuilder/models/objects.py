from ebuilder.models.vector import Vector
from ebuilder.models.particle import Particle
from ebuilder.services.statics import BLACK

import pygame

class Line():
    def __init__(self,
                p1: Vector,
                p2: Vector,
                color: tuple = BLACK):

        self.p1 = p1
        self.p2 = p2
        self.color = color

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.p1.coordinates, self.p2.coordinates)

    def update(self):
        pass

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
        
        pygame.draw.lines(screen, self.color, True, [
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
                left: float,
                top: float,
                width: float,
                height: float,
                speed: float,
                direction: float,
                mass:float = 0,
                gravity:float = 0,
                bounce:float = 0,
                friction:float = 0,
                color: tuple = BLACK):

        x = left + (width / 2) 
        y = top + (height / 2) 

        super().__init__(x, y, speed, direction, mass, gravity, bounce, friction)

        self.w = width
        self.h = height
        self.left = left
        self.top = top
        
        self.color = color

    @property
    def coordinates(self):
        return ((self.left, self.top), (self.w, self.h))

    @property
    def center(self):
        return (self.position.x, self.position.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.coordinates)

    def update(self):
        old = (self.x, self.y)
        super().update()

        self.left += self.x - old[0]
        self.top += self.y - old[1]

    def collision(self, p):
        if type(p) == Circle:
            return self.collisionCircle(p)
        elif type(p) == Rect:
            return self.collisionRect(p)
        else:
            return self.collisionParticle(p)

    def collisionRect(self, r1):
        x = False
        y = False

        if self.left >= r1.left and self.left <= r1.left + r1.w:
            x = True

        right = self.left + self.w
        if right <= r1.left and right >= r1.left + r1.w:
            x = True

        
        if self.top >= r1.top and self.top <= r1.top + r1.h:
            y = True

        btm = self.top + self.h
        if btm <= r1.top and btm >= r1.top + r1.h:
            x = True

        return x and y

    def collisionCircle(self, c1):
        cx = c1.position.x
        cy = c1.position.y
        
        if cx + c1.radius >= self.left and cx - c1.radius <= self.left + self.w:
            if cy + c1.radius >= self.top and cy - c1.radius <= self.top + self.h:
                return True
        return False

    def collisionParticle(self, p1):
        px = p1.position.x
        py = p1.position.y
        
        if px >= self.left and px <= self.left + self.w:
            if py >= self.top and py <= self.top + self.h:
                return True
        return False