from behaviour import *

import random

class RandomBehaviour(Behaviour):
    def decide(self, input):
        return random.randrange(5)
