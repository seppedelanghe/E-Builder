import math, pygame

from ebuilder.services.statics import BLUE, YELLOW
from ebuilder.models.objects import Circle
from ebuilder.models.environment import Env

WIDTH = 640
HEIGHT = 480

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False 

def update(entities: list):
    planet = entities['planet']
    sun = entities['sun']

    planet.gravitateTo(sun)


sun = Circle(HEIGHT / 2, HEIGHT / 2, 50, 0, 0, mass=25000, color=YELLOW)
planet = Circle(HEIGHT / 2 + 200, HEIGHT / 2, 5, 10, math.pi / 2, color=BLUE)

env = Env(update, events, size=(WIDTH, HEIGHT))

env.addEntity(sun, 'sun')
env.addEntity(planet, 'planet')
