from enum import Enum
import random

class Action(Enum):
    EAT = 0
    MOVE_UP = 1
    MOVE_RIGHT = 2
    MOVE_DOWN = 3
    MOVE_LEFT = 4

class Behaviour:
    pass

class RandomBehaviour(Behaviour):
    def decide(self, input):
        return random.choice([0, 1, 2, 3, 4])

class Animal:
    def __init__(self, behaviour):
        self.behaviour = behaviour

    def act(self, input):
        return self.behaviour.decide(input)

class Horse(Animal):
    pass

class Wolf(Animal):
    pass
