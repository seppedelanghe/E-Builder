from models.particle import Particle
from models.objects import Circle, Rect
from services.statics import *
import pygame

class Env:
    def __init__(self,
                updateHandler,
                eventHandler,
                size: tuple = (640, 480),
                background: tuple = WHITE,
                fps: int = 60):
        
        self.update = updateHandler
        self.events = eventHandler

        self.entities = {}

        self.size = size
        self.fps = fps
        self.bg = background

        self.running = False

    def _draw(self):
        for (name, e) in self.entities.items():
            e.update()
            e.draw(self.screen)

    def start(self):
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()

        self.running = True
        pygame.init()
        while self.running:
            self._loop()
        pygame.quit()

    def _loop(self):
        # Match set FPS
        self.clock.tick(self.fps)

        # Do event handeling
        self.events()

        # Set background
        self.screen.fill(self.bg)

        # Do updates
        self.update(self.entities)

        # Draw entities
        self._draw()

        # Flip display
        pygame.display.flip()

    def addEntity(self, entity, name: str):
        self.entities[name] = entity