import math, pygame, random

from ebuilder.models.objects import Circle
from ebuilder.models.environment import Env
from ebuilder.services.utils import randomInt

WIDTH = 640
HEIGHT = 480

def reuseDeadBall(ball: Circle):
    x = ball.position.x
    y = ball.position.y

    if x > WIDTH - ball.radius:
        ball.position.x = WIDTH - ball.radius
        ball.velocity.x = ball.velocity.x * ball.bounce
    if x < 0 + ball.radius:
        ball.position.x = 0 + ball.radius
        ball.velocity.x = ball.velocity.x * ball.bounce

    if y > HEIGHT - ball.radius:
        ball.position.y = HEIGHT - ball.radius
        ball.velocity.y = ball.velocity.y * ball.bounce
    if y < 0 + ball.radius:
        ball.position.y = 0 + ball.radius
        ball.velocity.y = ball.velocity.y * ball.bounce


def events(events):
    pass

def update(entities: dict):
    for (key, e) in entities.items():
        reuseDeadBall(e)


env = Env(update, events, size=(WIDTH, HEIGHT))

n_balls = 100

for i in range(n_balls):
    radius = randomInt(3, 5)
    ball = Circle(
        WIDTH / 2,
        HEIGHT,
        radius,
        radius * 10 / randomInt(2, 5),
        -math.pi / 2 + (random.random() - 0.5),
        mass=radius / 100,
        gravity=0.06,
        bounce=-0.6,
        friction=0
    )

    env.addEntity(ball, 'ball_{}'.format(i))