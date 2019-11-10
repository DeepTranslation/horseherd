from view import *
from world import *
from round import *

class App:
    width = 10
    height = 10

    rounds = 10
    loops = 50

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
                self.world.placeRandomly(animal)

            round = Round(i, self.loops, self.view, self.world, self.animals)
            round.on_execute()

if __name__ == "__main__":
    App().run()
