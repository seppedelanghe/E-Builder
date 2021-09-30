import math, pygame, random

from ebuilder.models.objects import Circle
from ebuilder.models.environment import Env
from ebuilder.services.utils import randomFloat, randomInt

WIDTH = 640
HEIGHT = 480


def events(events):
    pass

def update(entities: dict):
    drop = []
    for (key, e) in entities.items():
        if e.x > WIDTH + (e.radius * 2) or e.x < 0 - (e.radius * 2) or e.y < 0 - (e.radius * 2) or e.y > HEIGHT + (e.radius * 2):
            drop.append(key)

    for key in drop:
        entities.pop(key)

    if len(entities) == 0:
        env.running = False


env = Env(update, events, size=(WIDTH, HEIGHT))

n_balls = 100

for i in range(n_balls):
    radius = randomInt(3, 5)
    ball = Circle(
        WIDTH / 2,
        HEIGHT,
        radius,
        randomInt(4, 6),
        -math.pi / 2 + (randomFloat(1, 4) - 2),
        mass=0,
        gravity=0,
        bounce=-0,
        friction=0
    )

    env.addEntity(ball, 'ball_{}'.format(i))