import view 
import world
import rounds 
import animals

import cProfile


class App:
    width = 15
    height = 15

    rounds = 5
    loops = 100

    def __init__(self):
        self.view = view.View()
        self.animals = [
            animals.Horse.prototype(),
            animals.Horse.prototype(),
            animals.Horse.prototype(),
           # Horse.prototype(),
            animals.Wolf.prototype(),
            animals.Wolf.prototype(),
            #Wolf.prototype(),
        ]

        self.run()

    def run(self):
        pr = cProfile.Profile()
        pr.enable() 
        for i in range(self.rounds):
            self.world = world.World(self.width, self.height)

            for animal in self.animals:
                animal.alive = True
                self.world.placeRandomly(animal)
           
            round = rounds.Round(i, self.loops, self.view, self.world, self.animals)
            round.on_execute()
        pr.disable()
 
        pr.print_stats(sort='time')

if __name__ == "__main__":
    App().run()
