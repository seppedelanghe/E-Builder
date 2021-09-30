import math, pygame, random

from ebuilder.models.objects import Circle, Line
from ebuilder.models.vector import Vector
from ebuilder.models.environment import Env
from ebuilder.services.utils import randomFloat, spring

WIDTH = 640
HEIGHT = 480

K = Vector(0.05, 0.05)
SEPARATION = 200


# Pure visuals, no effect on springs
def edge(p: Circle):
    if p.x > WIDTH - p.radius:
        p.position.x = WIDTH - p.radius
        p.velocity.x = p.velocity.x * p.bounce
    if p.x < 0 + p.radius:
        p.position.x = 0 + p.radius
        p.velocity.x = p.velocity.x * p.bounce

    if p.y > HEIGHT - p.radius:
        p.position.y = HEIGHT - p.radius
        p.velocity.y = p.velocity.y * p.bounce
    if p.y < 0 + p.radius:
        p.position.y = 0 + p.radius
        p.velocity.y = p.velocity.y * p.bounce

def events(events):
    pass

def update(entities: dict):
    pA = entities['pA']
    pB = entities['pB']
    pC = entities['pC']

    spring(pA, pB, K, SEPARATION)
    spring(pB, pC, K, SEPARATION)
    spring(pA, pC, K, SEPARATION)

    edge(pA)
    edge(pB)
    edge(pC)

    pApB = entities['pApB']
    pBpC = entities['pBpC']
    pCpA = entities['pCpA']

    pApB.p1 = pA.position
    pApB.p2 = pB.position

    pBpC.p1 = pB.position
    pBpC.p2 = pC.position

    pCpA.p1 = pC.position
    pCpA.p2 = pA.position
       


env = Env(update, events, size=(WIDTH, HEIGHT))


# Particles
pA = Circle(
        randomFloat(WIDTH / 4, (WIDTH / 4 * 3)),
        randomFloat(0, HEIGHT),
        20,
        randomFloat(0, 50),
        randomFloat(0, math.pi * 2),
        friction=0.9,
        gravity=0.9
    )
env.addEntity(pA, 'pA')

pB = Circle(
        randomFloat(WIDTH / 4, (WIDTH / 4 * 3)),
        randomFloat(0, HEIGHT),
        20,
        randomFloat(0, 50),
        randomFloat(0, math.pi * 2),
        friction=0.9,
        gravity=0.9
    )
env.addEntity(pB, 'pB')

pC = Circle(
        randomFloat(WIDTH / 4, (WIDTH / 4 * 3)),
        randomFloat(0, HEIGHT),
        20,
        randomFloat(0, 50),
        randomFloat(0, math.pi * 2),
        friction=0.9,
        gravity=0.9
    )
env.addEntity(pC, 'pC')

# Lines between => Visual strings
env.addEntity(Line(pA.coordinates, pB.coordinates), 'pApB')
env.addEntity(Line(pB.coordinates, pC.coordinates), 'pBpC')
env.addEntity(Line(pC.coordinates, pA.coordinates), 'pCpA')