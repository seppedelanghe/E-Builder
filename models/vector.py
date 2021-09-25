import math

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Calculated properties
    @property
    def coordinates(self):
        return (self.x, self.y)

    @property
    def angle(self):
        return math.atan2(self.y, self.x)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # Setters
    def setAngle(self, angle):
        length = self.length
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length

    def setLength(self, length):
        angle = self.angle
        self.x = math.cos(angle) * length
        self.y = math.sin(angle) * length


    # Helpers
    def add(self, val: float):
        return Vector(self.x + val, self.y + val)

    def subtract(self, val: float):
        return Vector(self.x - val, self.y - val)

    def multiply(self, val: float):
        return Vector(self.x * val, self.y * val)

    def divide(self, val: float):
        return Vector(self.x / val, self.y / val)



    def v_add(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def v_subtract(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def v_multiply(self, v2):
        return Vector(self.x * v2.x, self.y * v2.y)

    def v_divide(self, v2):
        return Vector(self.x / v2.x, self.y / v2.y)

    def v_addTo(self, v2):
        self.x += v2.x
        self.y += v2.y

    def v_subtractFrom(self, v2):
        self.x -= v2.x
        self.y -= v2.y

    def v_multiplyBy(self, v2):
        self.x *= v2.x
        self.y *= v2.y

    def v_divideBy(self, v2):
        self.x /= v2.x
        self.y /= v2.y