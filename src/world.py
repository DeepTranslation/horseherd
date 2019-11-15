from animals import *
from enum import Enum

import random

class Terrain(Enum):
    SAND = (194, 178, 128)
    GRASS = (124, 252, 0)

class Tile:
    def __init__(self, terrain):
        self.terrain = terrain
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def remove(self, animal):
        self.animals = [a for a in self.animals if a != animal]

    def has(self, type):
        for animal in self.animals:
            if isinstance(animal, type):
                return True
        return False

    def toInt(self):
        t = 0
        if self.terrain == Terrain.GRASS:
            t = 1
        h = len(list(filter(lambda x: isinstance(x, Horse), self.animals)))
        w = len(list(filter(lambda x: isinstance(x, Wolf), self.animals)))

        return t * 100 + h * 10 + w
        #return ndarray(t, ,h, w)

class Outside(Tile):
    def __init__(self):
        pass

    def toInt(self):
        return -1

class World:
    width = 0
    height = 0

    def __init__(self, worldWidth, worldHeight):
        self.width = worldWidth
        self.height = worldHeight
        self.grid = []
        self.__createGrid()

    def __createGrid(self):
        for column in range(self.width):
            self.grid.append([])
            for row in range(self.height):
                terrain = random.choice([Terrain.SAND, Terrain.SAND, Terrain.SAND, Terrain.GRASS])
                self.grid[column].append(Tile(terrain))

    def getTile(self, x, y):
        if x < 0 or x >= self.width: return Outside()
        if y < 0 or y >= self.height: return Outside()

        return self.grid[x][y]

    def placeRandomly(self, animal):
        x = random.randrange(self.width)
        y = random.randrange(self.height)

        animal.x = x
        animal.y = y
        self.grid[x][y].add(animal)

    def getViewOf(self, animal):
        view = []

        v = animal.visualRange
        for x in range(animal.x - v, animal.x + v):
            for y in range(animal.y - v, animal.y + v):
                view.append(self.getTile(x, y).toInt())

        return view

    def eat(self, animal):
        self.getTile(animal.x, animal.y).terrain = Terrain.SAND

    def move_up(self, animal):
        self.move(animal, animal.x, animal.y, animal.x, animal.y - 1)

    def move_down(self, animal):
        self.move(animal, animal.x, animal.y, animal.x, animal.y + 1)

    def move_right(self, animal):
        self.move(animal, animal.x, animal.y, animal.x + 1, animal.y)

    def move_left(self, animal):
        self.move(animal, animal.x, animal.y, animal.x - 1, animal.y)

    def move(self, animal, old_x, old_y, new_x, new_y):
        if new_x < 0 or new_x >= self.width: return
        if new_y < 0 or new_y >= self.height: return

        self.getTile(old_x, old_y).remove(animal)
        self.getTile(new_x, new_y).add(animal)

        animal.x = new_x
        animal.y = new_y

    def fight(self, animal):
        tile = self.getTile(animal.x, animal.y)

        if len(tile.animals) == 1: return

        for other in tile.animals:
            if other == animal: continue

            if animal.attack > other.defense:
                other.alive = False
            elif animal.attack < other.defense:
                animal.alive = False
                break

        tile.animals = list(filter(lambda a: a.alive, tile.animals))
