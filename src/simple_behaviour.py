from behaviour import *

import random

class RandomBehaviour(Behaviour):
    def decide(self, input):
        return random.randrange(5)

class HunterBehaviour(Behaviour):
    pass

class FlightBehaviour(Behaviour):
    pass     
