import pygame

from models.objects import Triangle
from models.vector import Vector
from models.environment import Env

WIDTH = 640
HEIGHT = 480

states = {
    'steering': 0,
    'thrusting': 0,
}

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                states['thrusting'] = 1
            if event.key == pygame.K_LEFT:
                states['steering'] = -1
            if event.key == pygame.K_RIGHT:
                states['steering'] = 1
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                states['thrusting'] = 0
            if event.key == pygame.K_LEFT:
                states['steering'] = 0
            if event.key == pygame.K_RIGHT:
                states['steering'] = 0

def update(entities: list):
    ship = entities['ship']

    ship.angle += states['steering'] * 0.03

    thrust.x = states['steering'] * 0.03
    thrust.setAngle(ship.angle)
    thrust.setLength(0.1 if states['thrusting'] else 0)

    ship.accelerate(thrust)


tip = Vector(WIDTH * 0.1, HEIGHT / 2)
ship = Triangle(tip, 10, 0, 0, gravity=0.01, friction=0.02)
thrust = Vector(0,0)

env = Env(update, events, size=(WIDTH, HEIGHT))

env.addEntity(ship, 'ship')