import pygame, math

from ebuilder.models.objects import Triangle, Rect
from ebuilder.models.particle import Particle
from ebuilder.models.vector import Vector
from ebuilder.models.environment import Env
from ebuilder.services.utils import randomColor, randomInt
from ebuilder.services.statics import YELLOW

WIDTH = 320
HEIGHT = 480

states = {
    'flapping': 0,
    'delay': 0,
    'score': 0,
    'timer': 0
}

def make_walls():
    center = randomInt(HEIGHT / 4, HEIGHT / 4 * 3) # Random height of center
    spacing = 80 # Space to fly between
    width = 80 # Width of blocks
    color = YELLOW # color of blocks
    start = WIDTH # Where should the blocks spawn
    speed = 2
    direction = math.pi

    # Calculate height of top block
    height_a = HEIGHT * ((center - spacing) / HEIGHT)

    # Calculate top and height of bottom block
    top_b = center + (spacing / 2)
    height_b = HEIGHT - top_b

    # Create rectangles
    bA = Rect(start, 0, width, height_a, speed, direction, color=color)
    bB = Rect(start, top_b, width, height_b, speed, direction, color=color)

    return bA, bB
    

def moving_blocks():
    global env, states

    if (states['timer'] % 120) == 0:
        b1, b2 = make_walls()
        env.addEntity(b1, f"block_1_{states['timer']}")
        env.addEntity(b2, f"block_2_{states['timer']}")
        
def check_collision(entities: dict, agentKey: str):
    global env

    agent = entities[agentKey]

    for (k, e) in entities.items():
        if k != agentKey and e.collision(agent):
            print('Game over! You hit a wall.')
            env.running = False


def events(events):
    global states

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if states['delay'] == 0:
                    states['flapping'] = 1
                    states['delay'] = 10 # Disbale flapping for 10 rames

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                states['flapping'] = 0


def update(entities: dict):
    global states
    bird = entities['bird']

    if states['flapping']:
        bird.accelerate(Vector(0, -4))

    if states['delay'] > 0:
        states['flapping'] = 0
        states['delay'] -= 1

    moving_blocks()
    check_collision(entities, 'bird')

    states['timer'] += 1


nose = Vector(WIDTH * 0.1, HEIGHT / 2)
bird = Triangle(nose, 10, 2, 0, gravity=0.1, friction=0.03)

env = Env(update, events, size=(WIDTH, HEIGHT), fps=30)

env.addEntity(bird, 'bird')