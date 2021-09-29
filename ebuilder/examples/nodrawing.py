import math

from ebuilder.models.objects import Circle
from ebuilder.models.environment import Env

WIDTH = 640
HEIGHT = 480

RUN_FOR = 500

i = 0

def events():
    global i
    
    if i > RUN_FOR:
        i = 0

    if i == RUN_FOR: # Stop after n amount of runs
        env.running = False

    i += 1

def update(entities: list):
    planet = entities['planet']
    sun = entities['sun']

    planet.gravitateTo(sun)

    if env.running == False: # on last run, print coordinates of planet
        print(planet.coordinates)


sun = Circle(HEIGHT / 2, HEIGHT / 2, 50, 0, 0, mass=25000)
planet = Circle(HEIGHT / 2 + 200, HEIGHT / 2, 5, 10, math.pi / 2)

print(planet.coordinates)

env = Env(update, events, size=(WIDTH, HEIGHT), draw=False) # Size still important, no visuals but sets the size of the env

env.addEntity(sun, 'sun')
env.addEntity(planet, 'planet')
