from behaviour import *

import random

class RandomBehaviour(Behaviour):
    def decide(self, input):
        return random.randrange(6)

    def feedback(self, reward,state):
        pass

class HunterBehaviour(Behaviour):
    pass

class FlightBehaviour(Behaviour):
    pass
