from ebuilder.models.particle import Particle
from ebuilder.models.objects import Circle, Rect
from ebuilder.services.statics import *
import pygame

class Env:
    def __init__(self,
                updateHandler,
                eventHandler,
                size: tuple = (640, 480),
                background: tuple = WHITE,
                fps: int = 60,
                draw=True):
        
        self.update = updateHandler
        self.events = eventHandler

        self.entities = {}

        self.size = size
        self.fps = fps
        self.bg = background

        self.running = False
        self.drawVisuals = draw

    def _draw(self):
        for (name, e) in self.entities.items():
            e.draw(self.screen)

    def _updates(self):
        for (name, e) in self.entities.items():
            e.update()

    def start(self):
        if self.drawVisuals:
            self.screen = pygame.display.set_mode(self.size)
            self.clock = pygame.time.Clock()
            pygame.init()

            self.running = True
            while self.running:
                self._loop()

            pygame.quit()

        else:
            self.running = True
            while self.running:
                self._blindloop()

    def _blindloop(self):
        # Do user event handeling
        self.events()

        # Do user updates
        self.update(self.entities)

        # Update entities 
        self._updates()


    def _loop(self):
        # Match set FPS
        self.clock.tick(self.fps)

        # Do event handeling
        self.events()

        # Set background
        self.screen.fill(self.bg)

        # Do updates
        self.update(self.entities)

        # Update entities 
        self._updates()

        # Draw entities
        self._draw()

        # Flip display
        pygame.display.flip()

    def addEntity(self, entity, name: str):
        self.entities[name] = entity