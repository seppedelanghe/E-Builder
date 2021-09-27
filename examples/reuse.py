import math, pygame, random
from models.vector import Vector

from models.objects import Circle
from models.environment import Env
from services.utils import randomInt, randomColor

WIDTH = 640
HEIGHT = 480

def reuseDeadBall(ball: Circle):
    if ball.x > WIDTH + (radius * 2) or ball.x < 0 - (radius * 2) or ball.y < 0 - (radius * 2) or ball.y > HEIGHT + (radius * 2):
        ball.setPosition(Vector(WIDTH / 2, HEIGHT))
        ball.velocity.setLength(random.random() * 4 + 5)
        ball.velocity.setAngle(-math.pi / 2 + (random.random() - .5))


def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False 

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
        mass=0,
        gravity=0.06,
        bounce=-0,
        friction=0,
        color=randomColor()
    )

    env.addEntity(ball, 'ball_{}'.format(i))