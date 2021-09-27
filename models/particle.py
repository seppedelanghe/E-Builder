import math
from models.vector import Vector

class Particle:
    def __init__(self, 
                x: float, y: float,
                speed: float,
                direction: float,
                mass:float = 0,
                gravity:float = 0,
                bounce:float = 0,
                friction:float = 0):

        self.position = Vector(x, y)
        self.setVelocity(speed, direction)
        self.mass = mass
        self.gravity = Vector(0, gravity)
        self.bounce = bounce
        self.friction = Vector(friction, 0)

    @property
    def x(self):
        return self.position.x
    
    @property
    def y(self):
        return self.position.y

    def setX(self, x):
        self.position.x = x

    def setY(self, y):
        self.position.y = y

    def setPosition(self, coor: Vector):
        self.position = coor

    @property
    def coordinates(self):
        return self.position.coordinates

    def update(self):
        self.applyFriction()
        self.accelerate(self.gravity)
        self.position.v_addTo(self.velocity)

    def setVelocity(self, speed, direction):
        self.velocity = Vector(0, 0)
        self.velocity.setLength(speed)
        self.velocity.setAngle(direction)

    def accelerate(self, accel):
        self.velocity.v_addTo(accel)

    def angleTo(self, p2):
        return math.atan2(p2.position.y - self.position.y, p2.position.x - self.position.x)

    def distanceTo(self, p2):
        dx = p2.position.x - self.position.x
        dy = p2.position.y - self.position.y

        return math.sqrt(dx**2 + dy**2)

    def gravityTo(self, p2):
        grav = Vector(0, 0)
        dist = self.distanceTo(p2)

        grav.setLength(p2.mass / (dist * dist)) # M/r**2
        grav.setAngle(self.angleTo(p2))

        return grav

    def gravitateTo(self, p2):
        self.accelerate(self.gravityTo(p2))

    def applyFriction(self):
        self.friction.setAngle(self.velocity.angle)

        if self.velocity.length > self.friction.length:
            self.velocity.v_subtractFrom(self.friction)
        else:
            self.velocity.setLength(0)