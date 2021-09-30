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
                fpsCounter: bool = True):
        
        self.update = updateHandler
        self.events = eventHandler

        self.entities = {}

        self.size = size
        self.fps = fps
        self.fpsCounter = fpsCounter
        self.bg = background

        self.running = False

    def _draw(self):
        for (name, e) in self.entities.items():
            e.update()
            e.draw(self.screen)

        if self.fpsCounter:
            self.display_fps()

    def display_fps(self):
        font = pygame.font.SysFont("Arial", 12)
        fps = "FPS: " + str(int(self.clock.get_fps()))
        
        text_to_show = font.render(fps, 0, pygame.Color((0, 0, 0)))
        self.screen.blit(text_to_show, (10, 10))

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
        if self.fps > 0:
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