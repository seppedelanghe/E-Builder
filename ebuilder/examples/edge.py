import math, pygame, random

from ebuilder.models.objects import Circle
from ebuilder.models.environment import Env
from ebuilder.services.utils import randomInt

WIDTH = 640
HEIGHT = 480

def reuseDeadBall(ball: Circle):
    if ball.x > WIDTH + radius:
        ball.position.x = 0 - radius
    if ball.y > HEIGHT + radius:
        ball.position.y = 0 - radius

    if ball.x < 0 - radius:
        ball.position.x = WIDTH + radius
    if ball.y < 0 - radius:
        ball.position.y = HEIGHT + radius


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False 

def update(entities: dict):
    for (key, e) in entities.items():
        reuseDeadBall(e)


env = Env(update, events, size=(WIDTH, HEIGHT))

n_balls = 3

for i in range(n_balls):
    radius = randomInt(3, 5)
    ball = Circle(
        WIDTH / 2,
        HEIGHT,
        radius,
        randomInt(2, 5),
        -math.pi / 2 + random.random(),
        mass=0,
        gravity=0,
        bounce=-0,
        friction=0
    )

    env.addEntity(ball, 'ball_{}'.format(i))