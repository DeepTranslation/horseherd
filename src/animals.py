from simple_behaviour import *
from q_learning_behaviour import *

class Animal:
    def __init__(self, behaviour, attributes):
        self.x = 0
        self.y = 0
        self.alive = True
        self.age = 0
        self.behaviour = behaviour
        self.initiative = attributes.get('initiative', 0)
        self.visualRange = attributes.get('visualRange', 0)
        self.attack = attributes.get('attack', 0)
        self.defense = attributes.get('defense', 0)

    def act(self, input):
        return self.behaviour.decide(input)

    def feedback(self, reward):
        self.behaviour.feedback(reward)

class Horse(Animal):
    @staticmethod
    def prototype():
        return Horse(QLearningBehaviour(), {
            'visualRange': 3,
            'initiative': 1,
            'attack': 1,
            'defense': 2
        })

class Wolf(Animal):
    @staticmethod
    def prototype():
        return Wolf(RandomBehaviour(), {
            'visualRange': 4,
            'initiative': 2,
            'attack': 3,
            'defense': 2
        })
