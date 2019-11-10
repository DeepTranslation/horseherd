from pygame.locals import *
from random import randint
import pygame
import time
from enum import Enum

class Animal:
    x = 0
    y = 0
    step = 1
    direction = 0
    length = 1

   # updateCountMax = 2
    #updateCount = 0

    def __init__(self, x,y):
        self.x = x * self.step
        self.y = y * self.step

    def update(self):
        print(Terrain.SAND)
        Game.world[self.x][self.y].terrain = Terrain.SAND

      #  self.updateCount = self.updateCount + 1
       # if self.updateCount > self.updateCountMax:

        if self.direction == 0:
            self.x = self.x + self.step
        if self.direction == 1:
            self.x = self.x - self.step
        if self.direction == 2:
            self.y = self.y - self.step
        if self.direction == 3:
            self.y = self.y + self.step

       #     self.updateCount = 0

        print(self.x,self.y)
        Game.world[self.x][self.y].terrain = self.display_color

    def moveRight(self):
        self.direction = 0

    def moveLeft(self):
        self.direction = 1

    def moveUp(self):
        self.direction = 2

    def moveDown(self):
        self.direction = 3


    def target(self,dx,dy):
        if self.x > dx:
            self.moveLeft()

        if self.x < dx:
            self.moveRight()

        if self.x == dx:
            if self.y < dy:
                self.moveDown()

            if self.y > dy:
                self.moveUp()


    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x,self.y))


class Terrain(Enum):
    SAND = 0
    GRASS = 1
    HORSE = 2
    WOLF = 3


class Horse(Animal):
    display_color = Terrain.HORSE
    pass


class Wolf(Animal):
    display_color = Terrain.WOLF
    pass


class Food:
    x = 0
    y = 0
    step = 1

    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
        Game.world[self.x][self.y].terrain = Terrain.GRASS

    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))


class Tile:
    terrain = 0
    has_horse = False
    has_wolf = False

    def __init__(self, terrain):
        self.terrain = terrain


class Game:

    world = []

    def __init__(self, worldWidth, worldHeight):
        for row in range(worldHeight):
            self.world.append([])
            for column in range(worldWidth):
                tile = Tile(Terrain.SAND)
                self.world[row].append(tile)

    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False


class App:

    windowWidth = 800
    windowHeight = 600
    tileWidth = 10
    tileHeight = 10
    worldWidth = int(windowWidth / tileWidth)
    worldHeight = int(windowHeight / tileHeight)
    player = 0

    def __init__(self):
        self._running = True
        self._display_surf = None
        self._horse_surf = None
        self._wolf_surf = None
        self._food_surf = None
        self.game = Game(self.worldWidth, self.worldHeight)

        self.food = Food(8,5)
        self.horse = Horse(8,12)
        self.wolf = Wolf(12,8)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Horse Herd')
        self._running = True

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.horse.target(self.food.x, self.food.y)
        self.wolf.target(self.horse.x, self.horse.y)

        self.horse.update()
        self.wolf.update()

        if self.game.isCollision(self.food.x,self.food.y,self.horse.x, self.horse.y,self.tileWidth):
            self.food.x = randint(2,int(self.worldWidth)-20)
            self.food.y = randint(2,int(self.worldHeight)-20)
            Game.world[self.food.x][self.food.y].terrain = Terrain.GRASS

        if self.game.isCollision(self.horse.x,self.horse.y,self.wolf.x, self.wolf.y,self.tileWidth):
            self.horse.x = randint(2,int(self.worldWidth)-20)
            self.horse.y = randint(2,int(self.worldHeight)-20)

            pass

    def on_render(self):
        self.draw_world()
        pygame.display.flip()

    def draw_world(self):

        for row in range(self.worldHeight):
            for column in range(self.worldWidth):
                terrain = Game.world[row][column].terrain
                if terrain == Terrain.SAND:
                    color = (194, 178, 128)
                elif terrain == Terrain.GRASS:
                    color = (124, 252, 0)
                elif terrain == Terrain.HORSE:
                    color = (150,75,0)
                elif terrain == Terrain.WOLF:
                    color = (120, 120, 120)

                pygame.draw.rect(self._display_surf,
                             color,
                             [ column * self.tileWidth,
                               row * self.tileHeight,
                               self.tileWidth,
                               self.tileHeight])

#        background = pygame.transform.scale(Game.world, self.windowWidth, self.windowHeight)
 #       pygame.surfarray.blit_array(self._display_surf, background)


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while( self._running ):
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
