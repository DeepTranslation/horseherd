from view import *
from world import *

from pygame.locals import *
import pygame
import time

class App:

    width = 80
    height = 60

    def __init__(self):
        self._running = True
        self._view = View()

        self.world = World(self.width, self.height)
        self.horses = [Horse(RandomBehaviour())]
        self.wolves = [Wolf(RandomBehaviour())]

        for horse in self.horses:
            self.world.placeRandomly(horse)

        for wolf in self.wolves:
            self.world.placeRandomly(wolf)

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

        # if self.game.isCollision(self.food.x,self.food.y,self.horse.x, self.horse.y,self.tileWidth):
        #     self.food.x = random.randint(2,int(self.worldWidth)-1)
        #     self.food.y = random.randint(2,int(self.worldHeight)-1)
        #     Game.world[self.food.x][self.food.y].terrain = Terrain.SAND
        #
        # if self.game.isCollision(self.horse.x,self.horse.y,self.wolf.x, self.wolf.y,self.tileWidth):
        #     self.horse.x = random.randint(2,int(self.worldWidth)-1)
        #     self.horse.y = random.randint(2,int(self.worldHeight)-1)
        #     pass

        pass

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
