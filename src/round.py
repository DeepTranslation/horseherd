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
            state = self.world.getViewOf(animal)

            reward = 0
            # punishment for running out of the world
            tile = self.world.getTile(animal.x, animal.y)
            if isinstance( tile , Outside):
                reward -= 30

            # reward for eating
            if tile.terrain.GRASS:
                reward += 5

            #punishment for wolves close by
            wolves_in_proximity = 0


            proximity_wolves = 2
            
            for x in range(animal.x - proximity_wolves, animal.x + proximity_wolves):
                for y in range(animal.y - proximity_wolves, animal.y + proximity_wolves):
                    tile = self.world.getTile(x, y)
                    
                    if not isinstance( tile , Outside) and  tile.has(Wolf):
                     
                    #if self.tile.has(Wolf):
                       wolves_in_proximity += 1
                    
            reward += wolves_in_proximity*-10
            
            #reward for wolves close by
            horses_in_proximity = 0
            proximity_horses = 3
            for x in range(animal.x - proximity_horses, animal.x + proximity_horses):
                for y in range(animal.y - proximity_horses, animal.y + proximity_horses):
                    tile = self.world.getTile(x, y)
                    
                    if not isinstance( tile , Outside) and tile.has(Horse):
                       horses_in_proximity += 1
                    
            reward += horses_in_proximity*10
            
            if not animal.alive:
                reward = -100
            # TODO

            
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

            #time.sleep (10.0 / 1000.0);

        self.on_cleanup()
