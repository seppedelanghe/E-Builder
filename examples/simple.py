from models.environment import Env
from models.objects import Circle

import pygame, math

WIDTH = 640
HEIGHT = 480

# Handle PyGame events here
'''
For example:
- Clicks
- Mouse events
- Quit action
- etc.

Events get triggered every frame, before updates.
'''
def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            env.running = False 

# Handle entity updates here
'''
For example:
- Position
- Velocity
- Color
- etc.

Updates get triggered every frame, before drawing.
'''
def updates(entities: dict):
    pass # no action needed for this example

# Create an env that will create a window of 640px by 480px that runs at 30 FPS
env = Env(
    updates,
    events,
    size=(WIDTH, HEIGHT),
    fps=30)

# Create a ball (2D Circle) with fixed properties
ball = Circle(
        WIDTH / 2, # Middle of the screen
        HEIGHT, # Bottom of the screen
        radius=4, # Radius of 4 px
        speed=10,
        direction=-math.pi / 2, # Move up
        mass=0, # Mass of 0
        gravity=0, # no gravity
        bounce=-0, # no elasticity
        friction=0, # no friction => slowing down in air
        color=(0, 0, 0) # RBG Color black
    )

env.addEntity(ball, 'ball') # Adding the ball to the env
