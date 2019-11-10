from animals import *
from enum import Enum

import random

class Terrain(Enum):
    SAND = (194, 178, 128)
    GRASS = (124, 252, 0)

    @classmethod
    def list(self):
        return list(map(lambda c: c.value, Terrain))

class Tile:
    terrain = 0
    has_horse = False
    has_wolf = False

    def __init__(self, terrain):
        self.terrain = terrain

    def put(self, animal):
        if (isinstance(animal, Horse)):
            self.has_horse = True
        elif (isinstance(animal, Wolf)):
            self.has_wolf = True

class World:
    width = 0
    height = 0
    grid = []
    inhabitants = []

    def __init__(self, worldWidth, worldHeight):
        self.width = worldWidth
        self.height = worldHeight
        self.__createGrid()

    def __createGrid(self):
        for row in range(self.height):
            self.grid.append([])
            for column in range(self.width):
                terrain = random.choice(Terrain.list())
                self.grid[row].append(Tile(terrain))

    def generateHorse(self):
        self.grid[8][12].put(Horse())

    def generateWolf(self):
        self.grid[12][8].put(Wolf())

    def getTile(self, x, y):
        return self.grid[x][y]
