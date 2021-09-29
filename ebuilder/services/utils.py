import random
from ebuilder.models.particle import Particle
from ebuilder.models.vector import Vector
from ebuilder.services.statics import *

def randomColor():
    colors = [BLACK, WHITE, BLUE, RED, GREEN, YELLOW]
    return colors[randomInt(1, 6) - 1]

def randomFloat(min: float, max: float):
    return min + random.random() * (max - min)

def randomInt(min: int, max: int):
    return round(min + random.random() * (max - min))

def spring(p0: Particle, p1: Particle, k: Vector, separation: int):
    distance  = p0.position.v_subtract(p1.position)
    distance.setLength(distance.length - separation)

    springForce = distance.v_multiply(k)
    p1.velocity.v_addTo(springForce)
    p0.velocity.v_subtractFrom(springForce)