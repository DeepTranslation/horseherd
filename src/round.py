from view import *
from world import *

from pygame.locals import *
import pygame
import time

class Round:
    def __init__(self, num, loops, view, world, animals):
        self._running = True
        self._view = view
        self.world = world
        self.animals = animals
        self.num = num
        self.loops = loops
        self.currentLoop = 0

    def on_init(self):
        pygame.init()
        pygame.display.set_caption(str(self.num+1))
        

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        self._view.render(self.world)
        pygame.display.flip()

    def on_loop(self):
        self.currentLoop += 1
        if self.currentLoop >= self.loops:
            self._running = False
            return

        # Collect actions. Each animal sees the world as it is
        # and decides what to do. This mimicks everyone acting
        # at the same time.
        actions = []
        for animal in self.animals:
            input = self.world.getViewOf(animal)
            action = animal.act(np.asarray(input))
            actions.append((animal, action))

        # Execute the actions to update the world.
        for animal, action in actions:
            {
                0: lambda: self.world.eat(animal),
                1: lambda: self.world.move_up(animal),
                2: lambda: self.world.move_right(animal),
                3: lambda: self.world.move_down(animal),
                4: lambda: self.world.move_left(animal),
                5: lambda: self.world.fight(animal)
            }.get(action)()

        # Provide feedback
        for animal in self.animals:
            reward = 0
            if not animal.alive:
                reward = -10
            # TODO

            state = self.world.getViewOf(animal)
            animal.feedback(reward,state)

        # Remove animals that died
        self.animals = list(filter(lambda a: a.alive, self.animals))

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
