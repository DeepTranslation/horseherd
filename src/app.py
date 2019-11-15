from view import *
from world import *
from round import *

class App:
    width = 20
    height = 20

    rounds = 100
    loops = 100

    def __init__(self):
        self.view = View()
        self.animals = [
            Horse.prototype(),
            Horse.prototype(),
            Horse.prototype(),
            Horse.prototype(),
            Wolf.prototype(),
            Wolf.prototype(),
            Wolf.prototype(),
        ]

        self.run()

    def run(self):
        for i in range(self.rounds):
            self.world = World(self.width, self.height)

            for animal in self.animals:
                animal.alive = True
                self.world.placeRandomly(animal)

            round = Round(i, self.loops, self.view, self.world, self.animals)
            round.on_execute()

if __name__ == "__main__":
    App().run()
