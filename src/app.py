from view import *
from world import *
from behaviour import *
from simple_behaviour import *

from pygame.locals import *
import pygame
import time

class App:

    width = 2
    height = 2

    def __init__(self):
        self._running = True
        self._view = View()

        self.world = World(self.width, self.height)
        self.animals = [
            Horse(RandomBehaviour(), {'initiative': 1}),
            Wolf(RandomBehaviour(), {'initiative': 2})
        ]

        for animal in self.animals:
            self.world.placeRandomly(animal)

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Horses running wild!')

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._view.render(self.world)
        pygame.display.flip()

    def on_loop(self):
        self.animals.sort(key = lambda a: a.initiative, reverse = True)

        for animal in self.animals:
            input = self.world.getViewOf(animal)
            action = animal.act(input)

            {
                0: lambda: self.world.eat(animal),
                1: lambda: self.world.move_up(animal),
                2: lambda: self.world.move_right(animal),
                3: lambda: self.world.move_down(animal),
                4: lambda: self.world.move_left(animal)
            }.get(action)()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()

            keys = pygame.key.get_pressed()
            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()

            time.sleep (50.0 / 1000.0);

        self.on_cleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
