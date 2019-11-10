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
        self.animals.remove(animal)

    def has(self, type):
        for animal in self.animals:
            if isinstance(animal, type):
                return True
        return False

class World:
    width = 0
    height = 0
    grid = []

    def __init__(self, worldWidth, worldHeight):
        self.width = worldWidth
        self.height = worldHeight
        self.__createGrid()

    def __createGrid(self):
        for column in range(self.width):
            self.grid.append([])
            for row in range(self.height):
                terrain = random.choice([Terrain.SAND, Terrain.SAND, Terrain.SAND, Terrain.GRASS])
                self.grid[column].append(Tile(terrain))

    def getTile(self, x, y):
        return self.grid[x][y]

    def placeRandomly(self, animal):
        x = random.randrange(self.width)
        y = random.randrange(self.height)

        animal.x = x
        animal.y = y
        self.grid[x][y].add(animal)

    def getViewOf(self, animal):
        return []

    def move_down(self, animal):
        new_x = animal.x
        new_y = animal.y - 1

        self.getTile(animal.x, animal.y).remove(animal)
        self.getTile(new_x, new_y).add(animal)

        animal.x = new_x
        animal.y = new_y

    def move
