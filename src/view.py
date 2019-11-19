import world 
import animals 

import pygame

class View:

    tileWidth = 20
    tileHeight = 20

    def __init__(self):
        self._surface = None

    def render(self, world):
        windowWidth = world.width * self.tileWidth
        windowHeight = world.height * self.tileHeight

        self._surface = pygame.display.set_mode((windowWidth, windowHeight), pygame.HWSURFACE)

        for row in range(world.height):
            for column in range(world.width):
                tile = world.getTile(column, row)
                color = tile.terrain.value
                pygame.draw.rect(self._surface, color,
                    [ column * self.tileWidth,
                      row * self.tileHeight,
                      self.tileWidth,
                      self.tileHeight])

                if tile.has(animals.Wolf):
                    color = (120, 120, 120)
                    pygame.draw.ellipse(self._surface, color,
                    [ column * self.tileWidth,
                      row * self.tileHeight,
                      self.tileWidth,
                      self.tileHeight])
                if tile.has(animals.Horse):
                    color = (150, 75, 0)
                    pygame.draw.ellipse(self._surface, color,
                    [ column * self.tileWidth,
                      row * self.tileHeight,
                      self.tileWidth,
                      self.tileHeight])

                
